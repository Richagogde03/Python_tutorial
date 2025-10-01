# The Most Brilliant Exciting Fantastic Number
# medium

def describe_num(num):
    ans = "The most "

    if num % 1 == 0:
        ans += "brilliant "
    if num % 2 == 0:
        ans += "exciting "
    if num % 3 == 0:
        ans += "fantastic "
    if num % 4 == 0:
        ans += "virtuous "
    if num % 5 == 0:
        ans += "heart-warming "
    if num % 6 == 0:
        ans += "tear-jerking "
    if num % 7 == 0:
        ans += "beautiful "
    if num % 8 == 0:
        ans += "exhilarating "
    if num % 9 == 0:
        ans += "emotional "
    if num % 10 == 0:
        ans += "inspiring "

    ans += f"number is {num}!"
    print(ans)


describe_num(13)
describe_num(4)
describe_num(21)
describe_num(60)
