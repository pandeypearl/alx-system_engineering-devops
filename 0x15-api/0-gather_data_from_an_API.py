#!/usr/bin/python3
""" Script using JSONPlaceholder API to get info about employee """
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    json_o = res.json()
    print("Employee {} is done with tasks".format(json_o.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    task_l = []
    for task in tasks:
        if task.get('completed') is True:
            task_l.append(task)

    print("({}/{}):".format(len(task_l), len(tasks)))
    for task in task_l:
        print("\t {}".format(task.get("title")))
