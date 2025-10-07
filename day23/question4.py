# Count Substring
# Hard

def count_substring(string):
    count = 0
    for i in range(0, len(string)-1):
        if string[i] == "A":
            for j in range(i+1, len(string)):
                if string[j] == "X":
                    count = count + 1
    return count


print(count_substring("CAXAAYXZA"))
print(count_substring("AAXOXXA"))
print(count_substring("AXAXAXAXAX"))
