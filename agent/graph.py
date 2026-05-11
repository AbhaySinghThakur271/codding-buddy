from dotenv import load_dotenv
from langchain_core.globals import set_verbose, set_debug
from langchain_groq.chat_models import ChatGroq
from langgraph.constants import END
from langgraph.graph import StateGraph
from langgraph.prebuilt import create_react_agent

from agent.prompts import *
from agent.states import *
from agent.tools import write_file, read_file, get_current_directory, list_files

_ = load_dotenv()

set_debug(True)
set_verbose(True)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


def planner_agent(state: dict) -> dict:
    """Converts user prompt into a structured Plan."""
    user_prompt = state["user_prompt"]
    resp = llm.with_structured_output(Plan).invoke(
        planner_prompt(user_prompt)
    )
    if resp is None:
        raise ValueError("Planner did not return a valid response.")
    return {"plan": resp}


def architect_agent(state: dict) -> dict:
    """Creates TaskPlan from Plan."""
    plan: Plan = state["plan"]
    resp = llm.with_structured_output(TaskPlan).invoke(
        architect_prompt(plan=plan.model_dump_json())
    )
    if resp is None:
        raise ValueError("Planner did not return a valid response.")

    resp.plan = plan
    print(resp.model_dump_json())
    return {"task_plan": resp}

def validator_agent(state: dict):

    html = read_file.invoke({"path": "index.html"})

    if "<body>" not in html:
        raise ValueError("Invalid HTML")

    if len(html.strip()) < 100:
        raise ValueError("HTML too short")

    return state


def coder_agent(state: dict) -> dict:
    """LangGraph tool-using coder agent."""
    coder_state: CoderState = state.get("coder_state")
    if coder_state is None:
        coder_state = CoderState(task_plan=state["task_plan"], current_step_idx=0)

    steps = coder_state.task_plan.implementation_steps
    if coder_state.current_step_idx >= len(steps):
        return {"coder_state": coder_state, "status": "DONE"}

    current_task = steps[coder_state.current_step_idx]
    existing_content = read_file.invoke({"path": current_task.filepath})

    system_prompt = coder_system_prompt()
    all_files = list_files.invoke({"directory": "."})

    user_prompt = f"""
    You are building a COMPLETE frontend web application.

    CURRENT PROJECT FILES:
    {all_files}

    CURRENT TASK:
    {current_task.task_description}

    TARGET FILE:
    {current_task.filepath}

    EXISTING FILE CONTENT:
    {existing_content}

    IMPORTANT RULES:
    - Generate COMPLETE production-ready code.
    - NEVER leave files empty.
    - NEVER generate comments instead of implementation.
    - NEVER generate placeholders.
    - HTML must contain visible UI.
    - CSS must contain real styling.
    - JavaScript must contain working logic.
    - index.html must correctly link style.css and script.js.
    - The generated app must run directly in browser.
    - Always fully implement the requested feature.
    """

    coder_tools = [read_file, write_file, list_files, get_current_directory]
    react_agent = create_react_agent(llm, coder_tools)

    react_agent.invoke({"messages": [{"role": "system", "content": system_prompt},
                                     {"role": "user", "content": user_prompt}]})

    coder_state.current_step_idx += 1
    return {"coder_state": coder_state}


graph = StateGraph(dict)

graph.add_node("planner", planner_agent)
graph.add_node("architect", architect_agent)
graph.add_node("coder", coder_agent)
graph.add_node("validator", validator_agent)


graph.add_edge("planner", "architect")
graph.add_edge("architect", "coder")

graph.add_edge("coder", "validator")

graph.add_conditional_edges(
    "validator",
    lambda s: "END",
    {"END": END}
)

graph.set_entry_point("planner")
agent = graph.compile()
if __name__ == "__main__":
    result = agent.invoke({"user_prompt": "Build a colourful modern todo app in html css and js"},
                          {"recursion_limit": 100})
    print("Final State:", result)
