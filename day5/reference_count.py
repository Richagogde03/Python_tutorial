import sys

a = [1, 2, 3]

print(f"Reference count of object 'a': {sys.getrefcount(a)}")

b = a

# print(f"Reference count of object 'a' after creating reference 'b':
#       {sys.getrefcount(a)}")

del a

# print(f"Reference count of object after deleting reference 'a':
#     {sys.getrefcount(b)}")

del b
