import re
# HARD
# Cluster Vowels, Single Out Consonants


def split(string1):
    pattern = r"[^aeiou]|[aeiou]+"
    match = re.findall(pattern, string1)
    print(match)
    # ans = []
    # j = 0
    # for i in range(len(string1)):
    #     if string1[i] not in "aeiou":
    #         ans.append(string1[i])
    #     else:
    #         ans.append(match[j])
    #         j = j + 1
    return match


print(split("beautifully"))
print(split("spoonful"))
print(split("swimming"))
