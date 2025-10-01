import re
# RegEx XI-A: Whitespace Character Class
# Write the regular expression that will match all open compound words
# (separated by a space) starting with the word best and with a second word
# that begins with a b. Use the character class \s in your expression.
# MEDIUM


def whitespace_character(string):
    pattern = r"[b][e][s][t]\s[b]+[a-z]+"
    ans = re.findall(pattern, string)
    print(ans)


whitespace_character("""best buy best car best friend best-boy bestguest best "
"dressed best bet best man best deal best boyfriend""")
