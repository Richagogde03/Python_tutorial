
def arithmetic():
    expression = input("Enter the arithmetic expression : ")
    parts = expression.split()

    num1_str, operator, num2_str = parts

    num1 = int(num1_str)
    num2 = int(num2_str)

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '//':
        if num2 == 0:
            result = -1
        else:
            result = num1 // num2
    else:
        print("Invalid operator. Supported operators are +, -, *, and //.")
        return

    print(result)


arithmetic()
