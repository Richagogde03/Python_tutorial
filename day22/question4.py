# Do All Bigrams Exist?
# Medium

def can_find(list1, list2):
    for bigram in list1:
        found = False
        for word in list2:
            if bigram in word:
                found = True
                break
        if not found:
            return False

    return True


print(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))
print(can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]))
print(can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]))
