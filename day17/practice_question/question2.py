# Create a function that inverts the rgb values of a given tuple.
#  medium

def color_convert(r, g, b):
    my_list = []
    my_list.append(255-r)
    my_list.append(255-g)
    my_list.append(255-b)
    tup = tuple(my_list)

    return tup


print(color_convert(255, 255, 255))
print(color_convert(0, 0, 0))
print(color_convert(165, 170, 221))
