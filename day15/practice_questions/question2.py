# Create a function that takes two number strings
# and returns their sum as a string.

# medium

def add(string1, string2):
    int1 = 0
    int2 = 0
    if string1 == "" or string2 == "":
        print("Invalid Operation")
    else:
        int1 = int(string1)
        int2 = int(string2)
        a3 = int1 + int2
        print(a3)


add("111", "111")
add("10", "80")
add("", "20")
