# Todo: Create a c_to_f(temp) function
def c_to_f_temp(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return(temp_f)

# Todo: Create a list of reminders
reminders = ['Dr. appt @ 3pm','Softball @ 6pm','Grocery shopping']

# Todo: Get some input from the user
gratuity = input("What are you most grateful for today? --> ")

# Todo: Create a string with email content that includes:
#       - A greeting
#       - Some reminders
#       - 2-3 more items based on APIs that you've found
content = """
----------------------------------
Good morning, Mar. Hoy va a ser un buen dia!

Today you're grateful for {gratuity}. 

~~ Weather ~~

~~ Reminders ~~

~~ API STUFF ~~

"""

# Todo: Print the content to the console
print(content)