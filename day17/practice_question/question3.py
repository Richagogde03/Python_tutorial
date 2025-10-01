# Create a function to reproduce the wrap around effect shown:
# Example
# wrap_around("Hello, World!", 2) ➞ "llo, World!He"
# wrap_around("From what I gathered", -4) ➞ "eredFrom what I gath"
# wrap_around("Excelsior", 30) ➞ "elsiorExc"
# wrap_around("Nonscience", -116) ➞ "cienceNons"

# hard


def wrap_around(string, offset):
    ans = ""
    if offset > len(string):
        offset = offset % len(string)
    if offset < 0:
        offset = offset % len(string)
    offset_string = string[0:offset]
    ans = string[offset: len(string)] + offset_string
    return ans


print(wrap_around("Hello, World!", 2))
print(wrap_around("From what I gathered", -4))
print(wrap_around("Excelsior", 30))
print(wrap_around("Nonscience", -116))
