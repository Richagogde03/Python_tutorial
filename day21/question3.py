# Get Free Wi-Fi Anywhere You Go
# hard
import re

# def nonstop_hotspot(string1):
#     string2 = ""
#     count = 0
#     for i in string1:
#         if i == " ":
#             continue
#         else:
#             string2 += i
#     # print(string2)

#     for i in range(len(string2)):
#         if i + 1 < len(string2) and string2[i] == "P" and string2[i+1] == "*":
#             count = count + 1
#         elif i - 1 >= 0 and string2[i] == "P" and string2[i-1] == "*":
#             count = count + 1
#         else:
#             continue
#     return count


def nonstop_hotspot(string1):
    pattern = r'^[#][*]*[p][*]*^[#]]'
    ans = []
    string2 = ""
    for i in string1:
        if i == " ":
            continue
        else:
            string2 += i

    for i in string2:
        if i == "#":
            continue
        else:
            temp = re.findall(pattern, string2)
        # print(temp)
        ans.append(temp)
        # print(ans)
    ans2 = len(ans)-1
    return ans2


print(nonstop_hotspot("*   P  *   *"))
print(nonstop_hotspot("*  * #  * P # * #"))
print(nonstop_hotspot("***#P#***"))
print(nonstop_hotspot('#P#'))
print(nonstop_hotspot('P     *  # *'))
print(nonstop_hotspot('# *****  **  P     ** #    '))
