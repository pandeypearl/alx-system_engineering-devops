# 0x15. API

## Tasks

### 0. Gather data from an API
Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

Requirements:

<ul>
<li>You must use urllib or requests module</li>
<li>The script must accept an integer as a parameter, which is the employee ID</li>
<li>The script must display on the standard output the employee TODO list progress in this exact format:
<ul><li>First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
<ul><li>EMPLOYEE_NAME: name of the employee</li>
<li>NUMBER_OF_DONE_TASKS: number of completed tasks</li>
<li>TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks</li>
</ul></li>
<li>Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)</li>
</ul></li>
</ul>


### 1. Export to CSV
Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

<ul>
<li>Records all tasks that are owned by this employee</li>
<li>Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"</li>
<li>File name must be: USER_ID.csv</li>
</ul>


### 2. Export to JSON
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

<ul>
<li>Records all tasks that are owned by this employee</li>
<li>Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}</li>
<li>File name must be: USER_ID.json</li>
</ul>


### 3. Dictionary of list of dictionaries
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

<ul>
<li>Records all tasks from all employees</li>
<li>Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}</li>
<li>File name must be: todo_all_employees.json</li>
</ul>

