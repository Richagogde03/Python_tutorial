#  hard

# Create a class with a few functions like these examples.
# magic.replace("string", 'char', char') is a function that replaces all of
#  the specified characters with different specified characters.

# magic.str_length("string") is a function that returns the length of the
# string.

# magic.trim(" string ") is a function that returns a string with truncated
# spaces at both the beginning and end.

# magic.list_slice(list, tuple) is a function that returns the items in the
# list that are between the specified indexes. If the length of the new list
# is 0, return -1

class magic:
    def replace(self, string1, char1, char2):
        return string1.replace(char1, char2)

    def str_length(self, string):
        return len(string)

    def trim(self, string):
        return string.strip()

    def list_slice(self, string1, slicing):
        a1 = slicing[0] - 1
        a2 = slicing[1]
        return string1[a1:a2]


m1 = magic()
print(m1.replace("AzErty-QwErty", "E", "e"))
print(m1.str_length("hello world"))
print(m1.trim("      python is awesome      "))
print(m1.list_slice([1, 2, 3, 4, 5], (2, 4)))
