"""
Generate 100 random numbers. Write them to a file.
If the number is odd, end the line. The next number starts on a new line.
"""

text = ['I have eaten', 'the plums', 'that were in', 'the fridge']

with open('./examples/week_2/data/output.txt', 'w') as file:
    for line in text:
        file.write(line)
        file.write('\n')
