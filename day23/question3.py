# Calculated Bonus

def bonus(days):
    f_days = 0
    ans = 0
    if days > 0 and days < 32:
        return 0
    elif days > 33 and days < 40:
        f_days = days - 32
        ans = 32 * 0 + f_days * 325
    elif days > 41 and days < 48:
        f_days = days - 40
        ans = 32 * 0 + 8 * 325 + f_days * 550
    elif days > 48:
        f_days = days - 48
        ans = 32 * 0 + 8 * 325 + 8 * 550 + f_days * 600
    return ans


print(bonus(15))
print(bonus(37))
print(bonus(45))
print(bonus(50))
