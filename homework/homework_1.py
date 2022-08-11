import random

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
gratuity = input("What are you most grateful for today? --> ")

# weather
temp_hi = random.randint(10,35)
temp_low = temp_hi - random.randint(5,15)

# Todo: Create a string with email content that includes:
#       - A greeting
#       - Some reminders
#       - 2-3 more items based on APIs that you've found
content = f"""
----------------------------------
Good morning, Mar!

Today you're grateful for {gratuity}. 

~~ Weather ~~
Today's high: {temp_hi} degC ({round(c_to_f_temp(temp_hi))} degF)
Today's low: {temp_low} degC ({round(c_to_f_temp(temp_low))} degF)


~~ Reminders ~~
{reminders}

~~ API STUFF ~~

Hoy va a ser un buen dia!
----------------------------------
"""

# Todo: Print the content to the console
print(content)