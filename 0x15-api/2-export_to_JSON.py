#!/usr/bin/python3
""" Script using JSONPlaceholder API to get info about employee
and converts data to json """
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(user_id))

    name = user.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    todo_user = {}
    task_list = []

    for task in todos.json():
        if task.get('user_id') == int(user_id):
            task_dict = {
                        "task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')
                        }
            task_list.append(task_dict)
        todo_user[user_id] = task_list

    filename = user_id + '.json'
    with open(filename, mode='w') as f:
        json.dump(todo_user, f)
