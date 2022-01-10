import json
import csv
import random

f = open('data/tasks.csv', 'w', newline='')

# create the csv writer
writer = csv.writer(f)

row = ['xcord', 'ycord', 'required_time', 'delay']

# write a row to the csv file
writer.writerow(row)

tasks = list()

for i in range(100000):
    task = [
        random.randint(-100, 100),
        random.randint(-100, 100),
        float(random.randint(100, 5000) / 1000),
        random.randint(0, 60)
    ]
    tasks.append(task)

for task in tasks:
    writer.writerow(task)

# close the file
f.close()
