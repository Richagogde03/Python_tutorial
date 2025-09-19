import random

# print("Hii, Welcome to the number guessing game!!")

# total_chance = 7
# current_chance = 0
# lower_bound = int(input("Enter the lower bound : "))
# upper_bound = int(input("Enter the upper bound : "))

# print(f"You have 7 chances to guess the number between {lower_bound} and
# {upper_bound}")

# num = random.randint(lower_bound, upper_bound)
# guess = ""

# while current_chance < total_chance:
#     current_chance += 1
#     guess = int(input("Guess a number : "))
#     if guess == num:
#         print(f"Congratulation!!, you guessed the correct number in
# {current_chance} attempts.")
#         break

#     elif guess < num:
#         print("Too low, Please try again!!")
#     elif guess > num:
#         print("Too high, Please try again")
#     elif current_chance >= total_chance and num != guess:
#         print("You failed, better luck next time")


# using oops
class GuessNum:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def play_game(self):
        print("Welcome to the number guessing game!!\n")
        num = random.randint(self.min, self.max)

        self.choice = "y"

        while self.choice.lower() == "y":
            try:
                guess_num = int(input("Guess a number : \n"))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue
            if guess_num == num:
                print("Congratulations! you guessed it correct!!")
                break
            elif guess_num < num:
                print("Too low, Please try again!!")
            elif guess_num > num:
                print("Too high, Please try again!!")

            self.choice = input("Enter 'y' if want to continue else print 'x' : ")

            if self.choice.lower() == 'x':
                break


obj1 = GuessNum(1, 20)

obj1.play_game()
