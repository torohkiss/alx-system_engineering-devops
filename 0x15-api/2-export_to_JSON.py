#!/usr/bin/python3
"""
Use JSONPlaceholder API to get information about an employee
"""
import json
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

    user_name = "Antonette"

    user_tasks = {
        user_id: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_name
            } for task in data
        ]
    }
    #print(user_tasks)

    json_data = json.dumps(user_tasks)

    with open("USER_ID.json", 'w') as file:
        file.write(json_data)
