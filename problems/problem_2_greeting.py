"""
A program that takes as input:
    - your name
    - a weather condition
    - high temperature
    - low temperature

And prints a greeting:
    Good morning, {name}!
    Today is going to be {condition}.
    High: {high_c} °C ({high_f} °F)
    Low: {low_c} °C ({low_f} °F)

Scenario 2 practice
"""

# Todo: Get some input from the user
name = input("What's your name? --> ")
weather = input("What's the weather today? --> ")
temp_c_high = input("What's the high temp (degC)? --> ")
temp_c_low = input("What's the low today? --> ")

# Todo: Convert the temperatures
def c_to_f_temp(temp_c):
    pass

# Todo: Print the greeting
print("-------------------")
print(f"Good morning, {name}!")
print(f"Today is going to be {weather}")
print(f"")
print(f"")