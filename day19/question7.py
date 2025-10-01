# Burglary Series (05): Third Most Expensive
# HARD

def third_most_expensive(my_dict):
    max_f = 0
    max_s = 0
    max_t = 0
    ans = ""
    if len(my_dict) < 3:
        return False
    for key, value in my_dict.items():
        if value > max_f:
            max_t = max_s
            max_s = max_f
            max_f = value
        elif value > max_s and value < max_f:
            max_t = max_s
            max_s = value
        elif value > max_t and value < max_s:
            max_t = value

    for key, value in my_dict.items():
        if value == max_t:
            ans = key
            break

    return ans


print(third_most_expensive({}))
print(third_most_expensive({"piano": 100, "stereo": 200}))
print(third_most_expensive({"piano": 100, "stereo": 200, "tv": 10, "timmy": 500}))
