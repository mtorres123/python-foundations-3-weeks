import csv

with open('./examples/week_2/data/people.csv', 'r') as file:
    reader = csv.DictReader(file)

    for person in reader:
        print(f'{person["Name"]} is {person["Age"]}')


import pandas as pd
content = pd.read_csv("./examples/week_2/data/people.csv")
print(content.head(5))