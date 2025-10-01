def factorial(n):
    if n <= 0:
        return 1

    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


def trailing_zeros(number):
    fact = factorial(number)
    counter = 0

    while fact % 10 == 0:
        counter += 1
        fact //= 10
    return counter


print(trailing_zeros(10))
