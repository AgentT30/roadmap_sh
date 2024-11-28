# https://roadmap.sh/projects/task-tracker

import os
import sys
import json
import argparse
from typing import List
from datetime import datetime

class Task:
    def __init__(self, id: str):
        self.tasks_list_in_file = list_tasks()
        self.get_or_create_task(id)

    def get_or_create_task(self, id: int) -> None:
        """
            Gets the task object from the datastore if exists, else creates a new JSON object by creating a new ID

            Args:
                id (int): The id of the task to be fetched from the datastore

            Returns:
                None
        """
        if id:
            for task in self.tasks_list_in_file:
                if task['id'] == id:
                    self.id = id
                    self.description = task['description']
                    self.status = task['status']
                    self.createdAt = task['createdAt']
                    self.updatedAt = task['updatedAt']
        else:
            self.id = len(self.tasks_list_in_file) + 1
            self.description = None
            self.status = 'todo'
            self.createdAt = str(datetime.now())
            self.updatedAt = str(datetime.now())
        

    def add_task(self, description: str) -> int:
        """
            Saves the newly created task into the datastore

            Args:
                description (str): The description for the newly created task

            Returns:
                id (int): Id of the newly inserted task
        """
        self.description = description
        task_data = {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }

        self.tasks_list_in_file.append(task_data)

        self.write_to_file('tasks.json', self.tasks_list_in_file)
        
        return self.id
    
    def updated_task(self, description: str) -> int:
        """
            Updates the description of a task with the given description

            Args:
                description (str): The new description to be updated for the task

            Returns:
                id (int): Id of the task that is updated
        """
        self.description = description

        for index, task in enumerate(self.tasks_list_in_file):
            if task['id'] == self.id:
                self.tasks_list_in_file[index]['description'] = self.description
                self.tasks_list_in_file[index]['updatedAt'] = str(datetime.now())

                self.write_to_file('tasks.json', self.tasks_list_in_file)

                return self.id
        else:
            print("Task with the given ID not found in the datastore")
            
    def mark_task_status(self, status) -> int:
        """
            Marks the status of the task of the given ID

            Args:
                status (str): The new status to be updated for the task

            Returns:
                id (int): The ID of the task who's status is updated
        """
        self.status = status

        for index, task in enumerate(self.tasks_list_in_file):
            if task['id'] == self.id:
                self.tasks_list_in_file[index]['status'] = self.status
                self.tasks_list_in_file[index]['updatedAt'] = str(datetime.now())

                self.write_to_file('tasks.json', self.tasks_list_in_file)

                return self.id
        else:
            print("Task with the given ID not found in the datastore")
    
    def delete_task(self) -> int:
        """
            Deletes a task of the given ID in the datastore

            Args:
                None

            Returns:
                id (int): The ID of the task that is deleted
        """
        for index, task in enumerate(self.tasks_list_in_file):
            if task['id'] == self.id:
                del self.tasks_list_in_file[index]

                self.write_to_file('tasks.json', self.tasks_list_in_file)

                return self.id
        else:
            print("Task with the given ID not found in the datastore")

    @staticmethod
    def write_to_file(filename: str, data_to_be_written: List[dict]):
         """
            Writes the list of dicts into the given filename

            Args: 
                filename (str): The name of the file to be written
                data_to_be_written (List[dict]): The list of dicts to be written to the file

            Returns:
                None
         """
         with open(filename, 'w') as write_file:
                json.dump(data_to_be_written, write_file, indent=4)


def list_tasks(status: str = None) -> List[dict]:
    """
    Retrieves a list of tasks from the datastore, optionally filtered by status.

    Args:
        status (str, optional): The status to filter tasks by. Defaults to None.

    Returns:
        List[dict]: A list of tasks, each represented as a dictionary. If a status is provided,
                    only tasks with the matching status are returned. If the datastore file does
                    not exist, an empty list is returned and the file is created.
    """
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as read_file:
            tasks = json.load(read_file)

        if status:
            tasks = [task for task in tasks if task['status'] == status]
    else:
        """
            If the tasks.json file does not exist, create a new file by initializing an empty list in it
        """
        tasks = []
        with open('tasks.json', 'w') as write_file:
            json.dump(tasks, write_file, indent=4)

    return tasks



if __name__ == '__main__':
    """
        Setup the CLI argument parser and read the CLI arguments into variables
    """
    argparse = argparse.ArgumentParser()
    argparse.add_argument('--description', type=str)
    argparse.add_argument('--id', type=int, required=False)
    argparse.add_argument('--status', type=str, choices=['todo','in-progress', 'done'], required=False)
    argparse.add_argument('--operation', type=str, choices=['add', 'update', 'delete', 'list', 'mark'], required=True)
    args = argparse.parse_args()

    id = args.id
    status = args.status
    operation = args.operation
    description = args.description

    if operation == 'list':
        tasks_list = list_tasks(status)
        print(tasks_list)
    elif operation == 'add':
        if not description:
            print("--description argument is mandatory for adding a task")
            sys.exit(0)

        new_task = Task(None)
        new_task_id = new_task.add_task(description=description)

        if new_task_id:
            print(f"Task added successfully. (ID: {new_task_id})")
    elif operation == 'update':
        if not id:
            print("--id argument is mandatory for updating a task")
            sys.exit(0)

        if not description:
            print("--description argument is mandatory for updating a task")
            sys.exit(0)
        
        task_to_be_updated = Task(id=id)
        updated_task_id = task_to_be_updated.updated_task(description=description)

        if updated_task_id:
            print(f"Task with id {updated_task_id} has been updated!")
    elif operation == 'mark':
        if not id:
            print("--id argument is mandatory for marking a task")
            sys.exit(0)

        if not status:
            print(f"--status is a mandatory argument for marking a task")
            sys.exit(0)

        task_to_be_marked = Task(id=id)
        marked_task_id = task_to_be_marked.mark_task_status(status)

        if marked_task_id:
            print(f"Task with id {id} marked as {status} successfully")
    elif operation == 'delete':
        if not id:
            print("--id argument is mandatory for deleting a task")
            sys.exit(0)
        
        task_to_be_deleted = Task(id)
        deleted_task_id = task_to_be_deleted.delete_task()

        if deleted_task_id:
            print(f"Task with id {id} has been deleted! :-(")
    else:
        print(f"Invalid operation selected: {operation}")