import requests

BASE_URL = 'https://api.github.com'
USERNAME = 'ariannedee'
REPOSITORY = 'python-foundations-3-weeks'
ISSUE = 1
URL = f'{BASE_URL}/repos/{USERNAME}/{REPOSITORY}/issues/{ISSUE}/reactions'

valid_reactions = ['+1', '-1', 'laugh', 'confused', 'heart', 'hooray', 'rocket', 'eyes']

reaction = input(f"Enter one of these reactions: {valid_reactions} ")

if reaction not in valid_reactions:
    print(f"{reaction} is not a valid reaction")
    exit()
data = {'content': reaction}

headers = {
    'Authorization': 'bearer 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'
}
response = requests.post(URL, json=data, headers=headers)

print(f"{response.status_code} - {response.reason}")
