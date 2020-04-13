import os

f = open("data_file/example.com", "a")
print(f.tell())

print(os.stat("data_file/example.com").st_size)