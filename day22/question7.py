# Morse Code Decode
import re

my_dict = {
    "A": ".-", "B": "-...", "C":
    "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H":
    "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M":
    "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-",
    "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-",
    "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "0": "-----",
    "1": ".----", "2": "..---",
    "3": "...--", "4": "....-",
    "5": ".....", "6": "-....",
    "7": "--...", "8": "---..",
    "9": "----.", "&": ".-...",
    "'": ".----.", "@": ".--.-.",
    ")": "-.--.-", "(": "-.--.",
    ":": "---...", ",": "--..--", "=": "-...-",
    "!": "-.-.--", ".": ".-.-.-",
    "-": "-....-", "+": ".-.-.",
    '"': ".-..-.", "?": "..--..", "/": "-..-."
}


def decode_morse(string):

    # parts = re.split(r"( {1,})", string)
    # print(parts)
    # dots_to_char = {morse: char for char, morse in my_dict.items()}

    # ans = []
    # res = ""
    # for i in parts:
    #     for key, value in dots_to_char.items():
    #         if key == i:
    #             ans.append(value)
    #         elif i == '  ':
    #             ans.append(" ")
    # # print(ans)
    # res = res.join(ans)
    # return res

    dots_to_char = {morse: char for char, morse in my_dict.items()}
    parts = string.split(' '*3)
    # ans = ""
    decode_word = []
    for word in parts:
        decode_char = []
        chars = word.split()
        for char in chars:
            # print(char, end=" # ")
            decode_char.append(dots_to_char.get(char, " "))
        decode_word.append("".join(decode_char))
    return " ".join(decode_word)
    # ans = ' '.join(decode_word)
    # return ans


print(decode_morse(".... . .-.. .--.   -- .   -.-.--"))
print(decode_morse("-.-. .... .- .-.. .-.. . -. --. ."))
print(decode_morse(". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."))
print(decode_morse("-.. .. -..   -.-- --- ..-   --. --- -   -- -.--   -- .- .. .-..   ..--.."))
