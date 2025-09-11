
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num//2)):
        if num % i == 0:
            return False
    return True


def generate_prime(num):
    return [x for x in range(2, num+1) if is_prime(x)]


# armstrong number
def check_armstrong(num):
    digit = str(num)
    power = len(digit)
    result = 0

    for ch in digit:
        result += int(ch) ** power
        
    if num == result:
        return True
    else:
        return False


def generate_armstrong(num):
    return [x for x in range(1, num+1) if check_armstrong(x)]


def both_functions():
    print("Armstrong Numbers :- ", generate_armstrong(200))

    print("Prime Numbers :- ",  generate_prime(100))


both_functions()
