import os

# f = open("data_file/example.com", "a")
# print(f.tell())

# print(os.stat("data_file/example.com").st_size)

# print(f.truncate(37))
# f.close()

# f = open("data_file/example.com", "r")
# print(f.read())

# f = open("data_file/example.com", "r+")
# f.writelines("we are doing an 'r+' operation")
# f.close()

# f = open("data_file/example.com", "r+")
# f.writelines("In 'r' mode, the cursor is initally at the start of the file")
# f.close()

# f = open("data_file/example.com", "a+")
# f.writelines("\nWhat does writing in 'a+' do?")
# f.close()

os.rename("data_file/example.com", "data_file/example.txt")