#1 An App That Reads A Csv File, Then Converts The Output To Json
import csv
import json

with open('test.csv') as file:
    reader = csv.DictReader(file)

    x = []

    for row in reader:
        x.append(row)

    # y = {
    #     "Info": x
    # }

    z = json.dumps(x)

    print(z)

#What does lines 13-15 actually do?