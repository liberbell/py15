import csv

file = open("data_file/record.csv", "r")
with file:
    read = csv.DictReader(file)
    for row in read:
        print(dict(row))