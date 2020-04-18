import csv

# file = open("data_file/record.csv", "r")
# with file:
#     read = csv.DictReader(file)
#     for row in read:
#         print(dict(row))

csv.register_dialect("tab", delimiter = "\t")

file = open("data_file/record_tab.csv", "r")
with file:
    read = csv.reader(file, dialect="tab")
    for row in read:
        print(row)

csv.register_dialect("plus", delimiter = "+", lineterminator = "\n\n\r")

names = [["First Name", "Last Name"],
    ["Sofia", "Reyes"],
    ["Jerome", "Jackson"]
    ["Jia", "Zhong"]]

file = open("data_file/names_dialect.csv", "w")

with file:
    file_writer = csv.writer(file, dialect= "plus")