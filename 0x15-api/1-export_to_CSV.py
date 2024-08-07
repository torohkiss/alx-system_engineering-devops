#!/usr/bin/python3
"""
Exporting 0-gather_data_from_an_API.py to CSV
"""
import csv
import requests
import sys

if __name__ == "__main__":
    uid = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        uid)
    response = requests.get(user_url)
    username = response.json().get('username')
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        uid)
    todo = requests.get(todo_url).json()

    with open('{}.csv'.format(uid), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in todo:
            task_status = task.get('completed')
            task_title = task.get('title')
            writer.writerow([uid, username, task_status, task_title])
