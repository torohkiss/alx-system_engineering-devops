#!/usr/bin/python3
""" Python script that, using REST API, 
for a given employee ID, returns information 
about his/her TODO list progress.
"""

import requests
import sys

user_id = sys.argv[1]

apiurl = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

response_name = requests.get(apiurl)

user_name = response_name.json()['name']
print(user_name)

apiurl_todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
data_todos = requests.get(apiurl_todos)
data = data_todos.json()
total_num_tasks = len(data)
print(total_num_tasks)

apiurl_comp_tasks = "https://jsonplaceholder.typicode.com/todos?userId={}&completed=true".format(user_id)
data_comp = requests.get(apiurl_comp_tasks)
data_comp_true = data_comp.json()
num_comp_tasks = len(data_comp_true)
print(num_comp_tasks)

print("Employee {} is done with tasks({}/{}):".format(user_name, num_comp_tasks, total_num_tasks))

comp_task_titles = [task['title'] for task in data_comp_true]
for title in comp_task_titles:
	print('\t{}'.format(title))
