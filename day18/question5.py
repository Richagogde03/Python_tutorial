# Letters Shared Between Two Words
# Create a function that returns the number of characters shared between two
# words.

def shared_letters(string1, string2):
    set1 = set(string1)
    set2 = set(string2)
    count = 0
    # 1st method
    # for i in set1:
    #     for j in set2:
    #         if i == j:
    #             count += 1
    # return count

    # 2nd method
    common = set1.intersection(set2)
    for i in common:
        count += 1
    return count


print(shared_letters("apple", "meaty"))
print(shared_letters("class", "last"))
print(shared_letters("spout", "shout"))
shared_letters("fan", "forsook")
