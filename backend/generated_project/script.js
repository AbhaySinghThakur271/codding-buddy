let taskList = [];
let taskInput = document.getElementById('task-input');
let addTaskBtn = document.getElementById('add-task-btn');
let taskListElement = document.getElementById('task-list');

addTaskBtn.addEventListener('click', addTask);

taskInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        addTask();
    }
});

function addTask() {
    let task = taskInput.value.trim();
    if (task) {
        taskList.push(task);
        taskInput.value = '';
        renderTaskList();
    }
}

function renderTaskList() {
    taskListElement.innerHTML = '';
    taskList.forEach((task, index) => {
        let taskElement = document.createElement('li');
        taskElement.textContent = task;
        taskListElement.appendChild(taskElement);
    });
}
