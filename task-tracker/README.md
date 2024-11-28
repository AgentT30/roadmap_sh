Implementation of the project in Roadmap.sh https://roadmap.sh/projects/task-tracker

# Task-Tracker

Task-Tracker is a simple cli application that allows users to manage their tasks. User can create, read, update and delete tasks. The tasks are stored in a JSON file.

## Functionality

- Create a task
- Read all tasks
- Mark a task as 'done' or 'in-progress'
- Update a task
- Delete a task


## How to use

### List all the Tasks

`python3 task_tracker.py --operation list`


### List all the Tasks of a Specific Status

`python3 task_tracker.py --operation list --status todo`

### Add a new Task

`python3 task_tracker.py --operation add --description "New task detail"`

### Mark the Status of a Task as 'done'

`python3 task_tracker.py --operation mark --id 1 --status done`

### Update the description of a Task

`python3 task_tracker.py --operation update --id 1 --description "Updated Task Description"`

### Delete a Task

`python3 task_tracker.py --operation delete --id 1`