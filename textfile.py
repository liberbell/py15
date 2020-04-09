open("sample.txt")

file = open("sample.txt")

print(file)
print(file.mode)
print(file.closed)
file.close()
print(file.closed)

file = open("sample.txt")
print(file.read())

print(file.seek(0))
print(file.read(5))