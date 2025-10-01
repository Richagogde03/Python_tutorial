# Create a function (named fifth)
# that takes some arguments and returns the type of the fifth argument. In
# case the arguments were less than 5,
# return "Not enough arguments"

# medium

def fifth(l1):
    if len(l1) < 5:
        print("Not enough arguments")
    else:
        print(type(l1[4]))


fifth([1, 2, 3, 4, 5])
fifth(["a", 2, 3, [1, 2, 3], "five"])
fifth([1, 2, 3, 4])
