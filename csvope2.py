import csv

# file = open("data_file/record.csv", "r")
# with file:
#     read = csv.DictReader(file)
#     for row in read:
#         print(dict(row))

file = open("data_file/record_tab.csv", "r")
with file:
    read = csv.reader(file, dialect="tab")
    for row in read:
        print(row)