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
print(file.readline())