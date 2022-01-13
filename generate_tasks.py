import json
import csv
import operator
import random

f = open('data/tasks.csv', 'w', newline='')

# create the csv writer
writer = csv.writer(f)

row = ['xcord', 'ycord', 'required_time', 'delay']

# write a row to the csv file
writer.writerow(row)

tasks = list()

for i in range(1000):
    task = [
        random.randint(-100, 100),
        random.randint(-100, 100),
        float(random.randint(100, 5000) / 1000),
        random.randint(0, 240)
    ]
    tasks.append(task)

tasks.sort(key=operator.itemgetter(3))

for task in tasks:
    writer.writerow(task)

# close the file
f.close()
