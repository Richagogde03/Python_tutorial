

def convert_binary(num):
    digit = int(num)
    binary = ''

    if digit == 0:
        return '0'

    while digit > 0:
        binary = str(digit % 2) + binary
        digit = digit // 2

    return binary


num = input("Enter the number :- ")
result = convert_binary(num)
print(result)
