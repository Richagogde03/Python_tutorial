# """Write a program that returns a list
# of all the numbers from 1 to an integer
# argument. But for multiples of three
# use “Fizz” instead of the number and
# for the multiples of five use “Buzz”.
# For numbers which are multiples of both
# three and five use “FizzBuzz”."""

# Example = fizz_buzz(10) ➞ [1, 2, "Fizz", 4,
#  "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]

# medium

def fizz_buzz(num):
    result = []

    for i in range(1, num+1):
        if i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result


print(fizz_buzz(10))
