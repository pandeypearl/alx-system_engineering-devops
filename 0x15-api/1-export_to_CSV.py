#!/usr/bin/python3
""" Script using JSONPlaceholder API to get info about employee
and exporting data in CSV format """
import csv
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    user = '{}users/{}'.format(url, user_id)
    res = requests.get(user)
    json_o = res.json()
    name = json_o.get('username')

    todos = '{}todos?userId={}'.format(url, user_id)
    res = requests.get(todos)
    tasks = res.json()
    task_l = []
    for task in tasks:
        task_l.append([user_id,
                       name,
                       task.get('completed'),
                       task.get('title')])

    filename = '{}.csv'.format(user_id)
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in task_l:
            employee_writer.writerow(task)
