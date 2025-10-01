# Create a function that takes damage and speed (attacks per second) and
# returns the amount of damage after a given time.

# medium


def damage(damage, speed, time):
    if damage < 0 or speed < 0:
        return "Invalid"
    if time == "hour":
        return damage * speed * 60 * 60
    elif time == "minute":
        return damage * speed * 60
    elif time == "second":
        return damage * speed


# print(damage(40, 5, "second"))
# print(damage(100, 1, "minute"))
print(damage(2, 100, "hour"))
