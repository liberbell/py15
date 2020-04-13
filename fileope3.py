import os

# f = open("data_file/example.com", "a")
# print(f.tell())

# print(os.stat("data_file/example.com").st_size)

# print(f.truncate(37))
# f.close()

# f = open("data_file/example.com", "r")
# print(f.read())

f = open("data_file/example.com", "r+")
f.writelines("we are doing an 'r+' operation")
f.close()