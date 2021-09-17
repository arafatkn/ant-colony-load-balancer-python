import json
import csv
import random

f = open('data/datacenters.csv', 'w')

# create the csv writer
writer = csv.writer(f)

row = ['name', 'xcord', 'ycord', 'servers']

# write a row to the csv file
writer.writerow(row)

dcs = list()

for i in range(100):
    dc = ['DC' + str((i + 1)), random.randint(-100, 100), random.randint(-100, 100), random.randint(5, 10)]
    dcs.append({
        "name": dc[0],
        "x": dc[1],
        "y": dc[2],
        "servers": dc[3]
    })
    writer.writerow(dc)

# close the file
f.close()

json_data = json.dumps(dcs)

f = open("config/datacenters.json", "w")

f.write(json_data)

f.close()
