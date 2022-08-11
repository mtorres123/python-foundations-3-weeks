import json
import requests

URL = 'https://ariannedee.pythonanywhere.com/test_requests'

data = {
    'username': 'abcde',
    'password': '12345'
}

response = requests.post(URL, data=data)
print(f'{response.status_code} - {response.reason}')
if response.status_code >= 300:
    exit()

# json_data = json.dumps(data)
# headers = {'Content-Type': 'application/json'}
# response = requests.post(URL, data=json_data, headers=headers)
response = requests.post(URL, json=data)


print(response.text)

print(response.request.body)