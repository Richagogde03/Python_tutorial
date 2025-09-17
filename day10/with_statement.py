# without "with" , manual closing
file = open("Example2.txt", "r")
try:
    content = file.read()
    print(content)
finally:
    file.close()  # Ensures the file is closed


# Replacing Try-Except_finally with "with" statement
# using "with" while reading from a file
with open('demofile.txt', 'r') as file1:
    content1 = file1.read()
    print(content)

# writing to a file
with open("Example_with.txt", 'a') as file2:
    content2 = file2.write("Hello from us!!")
