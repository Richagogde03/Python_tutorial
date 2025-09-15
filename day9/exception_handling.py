# Question 1
numerator = int(input("Enter numerator value : "))
denomenator = int(input("Enter denominator value : "))


# def safe_divide(numerator, denomenator):
#     try:
#         result = numerator // denomenator
#         return result
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero!!")
#         return None


# print(safe_divide(numerator, denomenator))


# Que2. try, except, else
# try:
#     user_input = input("Please enter an integer: ")
#     number = int(user_input)
# except ValueError:
#     print("That was not a valid integer!")
# else:
#     print(f"You entered a valid integer: {number}")


# Que3. try, except, else and finally
def safe_division(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"The result of the division is: {result}")
    finally:
        print("Division attempt finished.")


# Test cases
safe_division(10, 2)
safe_division(5, 0)
safe_division(20, 4)
