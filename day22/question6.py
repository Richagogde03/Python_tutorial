# Making a Sandwich
# medium


def make_sandwich(list1, flavour):
    ans = []
    for i in list1:
        if i == flavour:
            ans.append("bread")
            ans.append(i)
            ans.append("bread")
        else:
            ans.append(i)
    return ans


print(make_sandwich(["tuna", "ham", "tomato"], "ham"))
print(make_sandwich(["cheese", "lettuce"], "cheese"))
print(make_sandwich(["ham", "ham"], "ham"))
print(make_sandwich(["t", "h", "t"], "h"))
