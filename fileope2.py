# file = open("data_file/example.com", "w")
# file.write("Let's check the write operation.")
# file.seek(6)

# file.write(" examine ")
# file.close()

# file = open("data_file/example.com", "r")
# for lines in file :
#     print(lines)
# file.close()

# with open("data_file/example.com", "w") as f:
#     f.write("First line\n")
#     f.write("Second line\n")
#     f.write("Third line\n")

# f = open("data_file/example.com", "a")
# print(f.tell())

# f.writelines(["Another line was appended\n",
# "What will it look like now?\n",
# "Let check it out\n"])

f = open("data_file/example.com", "r")
print(f.readlines())

f.close()