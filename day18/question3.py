"""Write a function that takes a positive integer num and calculates how many
dots exist in a pentagonal shape around the center dot on the Nth iteration.

In the image below you can see the first iteration is only a single dot. On
the second, there are 6 dots. On the third, there are 16 dots, and on the
fourth there are 31 dots."""


# hard
def pentagonal(num):
    ans = 1
    for i in range(0, num):
        ans += 5 * i
    return ans


print(pentagonal(1))
print(pentagonal(2))
print(pentagonal(3))
print(pentagonal(8))
