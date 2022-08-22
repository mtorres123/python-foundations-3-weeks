# from pprint import pprint
import random
import sys

import requests

base_url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'appid':'<>',
    'lat': 43.6422222,
    'lon': -72.2522222,
    'units': 'metric'
}

headers = {
    'content-type': 'application/json'
}

response = requests.get(base_url,headers=headers,params=params)
response.raise_for_status()
data = response.json()

# Todo: Create a c_to_f(temp) function
def c_to_f_temp(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return(temp_f)

# assert c_to_f_temp(0) == 32, f"Got {c_to_f_temp(0)}"
# assert round(c_to_f_temp(36.5)) == 98, f"Got {round(c_to_f_temp(36.5))}"
# assert False, f'Error message'

# consider pytest module

# Todo: Create a list of reminders
reminders = """Dr. appt @ 3pm
Softball @ 6pm
Grocery shopping
"""

# Todo: Get some input from the user
# gratuity = input("What are you most grateful for today? --> ")

# weather
weather = data['weather'][0]
temps = data['main']
temp_hi = temps['temp_max']
temp_low = temps['temp_min']

# Todo: Create a string with email content that includes:
#       - A greeting
#       - Some reminders
#       - 2-3 more items based on APIs that you've found
content = f"""
----------------------------------
Good morning, Marissa!

~~ Weather ~~
Today is going to be {weather['main'].lower()}.
High: {temp_hi} degC ({round(c_to_f_temp(temp_hi))} degF)
Low: {temp_low} degC ({round(c_to_f_temp(temp_low))} degF)
Humidity: {temps['humidity']}%


~~ Reminders ~~
{reminders}

~~ API STUFF ~~

Hoy va a ser un buen dia!
----------------------------------
"""

# Todo: Print the content to the console
print(content)
# pprint(data)
