# JSON HANDLING FOR STRUCTURED DATA

import json # import the json module

with open('./config.json') as json_file:
    config = json.load(json_file)

    print(config)
    print(type(config))

    print(config["default_parameters"]["temperature"])
    print(config["user_prompts"]["farewell_message"])

# PARSING JSON DATA FROM API RESPONSES

import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')

print(response)

# Status Codes
# 2xx Successful responses
# 3xx Redirection messages
# 4xx Client error responses
# 5xx Server error responses

data = response.json()
# data = json.loads(response.text)
print(data)

print(data[99]["id"])
