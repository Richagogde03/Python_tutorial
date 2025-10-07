# Look and Say Numbers
# hard

def look_and_say(num):
    n1 = str(num)
    if len(n1) % 2 != 0:
        return "Invalid"

    for i in range(0, len(n1)-1, 2):
        f_num = int(n1[i])
        s_num = n1[i+1]
        for j in range(0, f_num):
            print(s_num, end="")


look_and_say(3132)
print()
look_and_say(95)
print()
look_and_say(120520)
print()
print(look_and_say(231))
