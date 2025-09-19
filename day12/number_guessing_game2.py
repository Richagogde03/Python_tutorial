import random


def game_decorator(func):
    def wrapper(self):
        print("Starting the game...")
        func(self)
        print("Game over.")
    return wrapper


class GuessNum:
    def __init__(self, min_val, max_val):
        self._min = min_val
        self._max = max_val
        self.guess_count = 0

    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, value):
        if value < 0:
            print("Minimum value cannot be negative.")
        else:
            self._min = value

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, value):
        if value < self._min:
            print("Maximum value cannot be less than the minimum value.")
        else:
            self._max = value

    @game_decorator
    def play_game(self):
        print("Welcome to the number guessing game!!\n")
        num = random.randint(self.min, self.max)

        self.choice = "y"
        self.guess_count = 0

        while self.choice.lower() == "y":
            try:
                guess_num = int(input(f"Guess a number between {self.min} and {self.max}: "))
                self.guess_count += 1
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue

            if guess_num < self.min or guess_num > self.max:
                print(f"Please guess within the range of {self.min} and {self.max}.")
                continue

            if guess_num == num:
                print(f"Congratulations! you guessed it correct in {self.guess_count} guesses!!")
                break
            elif guess_num < num:
                print("Too low, Please try again!!")
            elif guess_num > num:
                print("Too high, Please try again!!")

            self.choice = input("Enter 'y' if want to continue else print 'x' : ")

            if self.choice.lower() == 'x':
                print(f"You ended the game after {self.guess_count} guesses.")
                break


obj1 = GuessNum(1, 20)
obj1.min = 5
obj1.max = 50
obj1.play_game()
