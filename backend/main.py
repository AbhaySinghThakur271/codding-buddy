from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pathlib
import shutil
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request

from agent.graph import agent

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PROJECT_ROOT = pathlib.Path.cwd() / "generated_project"

app.mount(
    "/preview",
    StaticFiles(directory=PROJECT_ROOT),
    name="preview"
)

class PromptRequest(BaseModel):
    prompt: str


@app.post("/api/generate")
async def generate(req: PromptRequest, request: Request):

    # clear previous project
    if PROJECT_ROOT.exists():
        shutil.rmtree(PROJECT_ROOT)

    PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    result = agent.invoke(
        {"user_prompt": req.prompt},
        {"recursion_limit": 100}
    )

    files = []

    for file in PROJECT_ROOT.glob("**/*"):
        if file.is_file():
            files.append(str(file.relative_to(PROJECT_ROOT)))

    preview_file = None

    priority_files = [
        "index.html",
        "templates/index.html"
    ]

    for p in priority_files:

        full_path = PROJECT_ROOT / p

        if full_path.exists():
            preview_file = p
            break

    if preview_file is None:

        for file in files:
            if file.endswith(".html"):
                preview_file = file
                break

    return {
        "files": files,
        "preview_url": f"{request.base_url}preview/{preview_file}" if preview_file else None
    }
