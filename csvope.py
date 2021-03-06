import csv

file = open("data_file/record.csv", "r")
with file:
    read = csv.reader(file)
    for row in read:
        print(row)

file = open("data_file/record_pipe.csv", "r")
with file:
    read = csv.reader(file, delimiter="|")
    for row in read:
        print(row)

file = open("data_file/record_tab.csv", "r")
with file:
    read = csv.reader(file, delimiter="\t")
    for row in read:
        print(row)