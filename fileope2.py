# file = open("data_file/example.com", "w")
# file.write("Let's check the write operation.")
# file.seek(6)

# file.write(" examine ")
# file.close()

file = open("data_file/example.com", "r")
for lines in file :
    print(lines)
file.close()

