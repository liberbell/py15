file = open("data_file/example.com", "w")
file.write("Let's check the write operation.")
file.seek(6)

file.write(" examine ")
file.close()