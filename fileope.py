file = open("data_file/sample.txt")

print(file.tell())

print(file.read(5))

print(file.tell())

file.seek(0)
print(file.read(5))

print(file.readline())
print(file.readline())
print(file.readline())

file.seek(0)
print(file.readlines())

file.close()

with open("data_file/sample.txt") as f:
    data = f.readlines()
print(data)
print(f.closed)


with open("data_file/sample.txt") as f:
    line = f.readline()

    while line:
        print(line)
        line = f.readline()
