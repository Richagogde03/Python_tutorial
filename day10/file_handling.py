
# file_object = open("demofile.txt", 'r')
# # reading entire file
# content = file_object.read()
# print(content)
# file_object.close()

# # Reading one line a time
# file = open("demofile.txt", 'r')
# content2 = file.readline()
# content3 = file.readlines()
# print(content2)
# print(content3)
# file.close()

# writing to a file (overwrites existing content)
# file1 = open("Example2.txt", 'w')
# file1.write("Today's date is 16th sept.")
# file1.close()

# write mode (overwrite)
# file1 = open("demofile.txt", 'w')
# file1.write("Today's date is 16th sept.")
# file1.close()

# append mode
file1 = open("demofile.txt", 'a')
file1.write("\nHello people")
file1.writelines("\nKeys, tables etc.")
file1.close()
