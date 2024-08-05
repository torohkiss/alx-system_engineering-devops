#!/usr/bin/python3
"""
Exporting 0-gather_data_from_an_API.py to CSV
"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    apiurl = "https://jsonplaceholder.typicode.com/users/{}".format(
        user_id)

    response_name = requests.get(apiurl)

    user_name = response_name.json()['name']

    ai = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    data_todos = requests.get(ai)
    data = data_todos.json()
    total_num_tasks = len(data)

    ac = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        "&completed=true".format(user_id)
    data_comp = requests.get(ac)
    data_comp_true = data_comp.json()
    num_comp_tasks = len(data_comp_true)

    #print("Employee {} is done with tasks({}/{}):".format(
    #    user_name, num_comp_tasks, total_num_tasks))

    comp_task_titles = [task['title'] for task in data_comp_true]
    #for title in comp_task_titles:
    #    print('\t {}'.format(title))

    with open('USER_ID.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"])
        for task in data:
            writer.writerow([user_id, user_name, task['completed'], task['title']])
