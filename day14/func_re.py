import re
from re import split


# 1. findall()
# text1 = """Hello my number is 12345466
# and my friend number is 9836827998"""
# pattern1 = '\d+'
# match1 = re.findall(pattern1, text1)
# print(match1)


# 2. re.compile(),compile re into pattern object
text2 = """Hello, i am Mr. giberson"""
# match2 = re.compile("[a-m]")
# print(match2.findall(text2))


# 3. compile + findall
text3 = "I went to him at 11 A.M. on 4th July 1886"
# for single digit
# match3 = re.compile("\\d")
# print(match3.findall(text3))
# for multiple digits or sequence
# match4 = re.compile("\d+")
# print(match4.findall(text3))


# 4. Word and non-word characters
# \w matches single word character
# text4 = re.compile('\w')
# print(text4.findall("He said *** in some language"))

# \w+ to match group of word character
# text5 = re.compile('\w+')
# print(text5.findall("""I went to him at
#                     11 A.M., he \\\ said **## in some_langauge"""))
# match5 = re.findall("\w+", """I went to him at
#                     11 A.M., he \\\ said **## in some_langauge""")
# print(match5)

# \W for non-word character
# text6 = re.compile('\W')
# print(text6.findall("He said ** ## will you__come "))


# all occurence of ab*
# text7 = re.compile("ab*")
# print(text7.findall("ababbbabba"))


# re.split(),
# non worded charcater
# print(split('\\W+', 'Words, words , Words'))
# print(split('\\W+', "Word's words Words"))
# print(split('\\W+', 'On 12th Jan 2016, at 11:02 AM'))
# using digits
# print(split('\\d+', 'On 12th Jan 2016, at 11:02 AM'))

# using maxsplit and flags
print(re.split('\\d+', 'On 12th Jan 2016, at 11:02 AM', 1))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))


# re.sub()
