# WordRank Scoring System
# Create a function that takes a string of words and returns the highest
# scoring word. Each letter of a word scores points according to it's position
# in the alphabet: a = 1, b = 2, c = 3, etc.

# HARD

def word_rank(string):
    my_dict = {
        "a": 1, "b": 2, "c": 3, 'd': 4,
        "e": 5, "f": 6, "g": 7, "h": 8,
        "i": 9, "j": 10, "k": 11, "l": 12,
        "m": 13, "n": 14, "o": 15, "p": 16,
        "q": 17, "r": 18, "s": 19, "t": 20,
        "u": 21, "v": 22, "w": 23, "x": 24,
        "y": 25, "z": 26
    }
    splitting = string.split(" ")
    ans_char = ""
    sum = 0
    res = ""
    for i in range(len(splitting)):
        char = splitting[i]
        curr_sum = 0
        for j in char.lower():
            if j == "." or j == "!" or j == ",":
                continue
            j = my_dict[j]
            curr_sum = curr_sum + j

        if curr_sum > sum:
            sum = curr_sum
            ans_char = char

    for i in ans_char:
        if i == "!" or i == "," or i == ".":
            continue
        else:
            res = res + i

    print(res)


word_rank("The quick brown fox")
word_rank("Nancy is very pretty.")
word_rank("Check back tomorrow, man!")
word_rank("Wednesday is hump day.")
