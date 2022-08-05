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
temp_c_high = float(input("What's the high temp (degC)? --> "))
temp_c_low = float(input("What's the low today? --> "))

# Todo: Convert the temperatures
def c_to_f_temp(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return(temp_f)

temp_f_high = c_to_f_temp(temp_c_high)
temp_f_low = c_to_f_temp(temp_c_low)

# Todo: Print the greeting
print(f"""
-------------------------------------------
Good morning, {name}!
Today is going to be {weather}
High: {temp_c_high} degC ({temp_f_high} degF)
Low: {temp_c_low} degC ({temp_f_low} degF)
-------------------------------------------
""")

# print("-------------------")
# print(f"")
# print(f"Today is going to be {weather}")
# print(f"High: {temp_c_high} degC ({temp_f_high} degF)")
# print(f"Low: {temp_c_low} degC ({temp_f_low} degF)")