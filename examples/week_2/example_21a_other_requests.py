# import requests

# URL = 'https://automatetheboringstuff.com/'

# # to inform the API of who is requesting
# name = input("Your name: ")
# email = input("Your email: ")

# headers = {'User-Agent': f'{name} ({email})'}
# response = requests.get(URL, headers=headers)

# print(f'{response.status_code} - {response.reason}')

# if response.status_code >= 300:
#     exit()

# filename = './examples/week_2/data/get_output.html'

# with open(filename, 'w', encoding="utf-8") as file:
#     file.write(response.text)

# print(f'File saved to "{filename}"')

# ---------------------------------------------
import requests
import csv
import pandas as pd
from pprint import pprint

BASE_URL = 'https://api.github.com'
USERNAME = 'ariannedee' 
REPOSITORY = 'python-foundations-3-weeks' 
ISSUE = 1
URL = f'{BASE_URL}/repos/{USERNAME}/{REPOSITORY}/issues/{ISSUE}'

response = requests.get(URL)

print(f"{response.status_code} - {response.reason}")
if response.status_code >= 300:
    exit()

data = response.json()
reactions = data['reactions']
pprint(reactions)

reactions_to_csv = []
for reaction, count in reactions.items():
    if reaction in ['url', 'total_count']:
        continue
    row = {
        'Reaction': reaction,
        'Count': count
    }
    reactions_to_csv.append(row)

pprint(reactions_to_csv)

reaction_to_emoji = {
    "+1": '👍',
    "-1": '👎',
    "laugh": '😄',
    "hooray": '🎉',
    "confused": '😕',
    "heart": '❤️',
    "rocket": '🚀',
    "eyes": '👀'
}

output_str = ''
for reaction in reactions_to_csv:
    name = reaction['Reaction']
    as_emoji = reaction_to_emoji[name]
    count = reaction['Count']
    output_str += (as_emoji + ' ') * count

print(output_str)
