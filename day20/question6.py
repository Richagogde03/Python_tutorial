# shadow sentences
# HARD

def shadow_sentence(string1, string2):
    len_str1 = len(string1)
    len_str2 = len(string2)
    if len_str1 != len_str2:
        return False

    for i in range(len(string1)):
        for j in range(len(string2)):
            if string1[i] == string2[i]:
                return False
            else:
                return True


print(shadow_sentence("they are round", "fold two times"))
print(shadow_sentence("own a boat", "buy my wine"))
print(shadow_sentence("his friends", "our company"))
print(shadow_sentence("salmonella supper", "birthright"))
print(shadow_sentence('impossible poetry', 'gargantuan cliffs'))
