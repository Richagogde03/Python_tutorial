
# Create a function that takes an array of values resistance that are
# connected in series, and calculates the total resistance of the circuit in
# ohms. The ohm is the standard unit of electrical
# resistance in the International System of Units ( SI ).

# medium

def series_resistance(list1):
    sum = 0
    for i in list1:
        sum = sum + i
    result = (f'"{sum} ohms"')

    return result


list1 = [1, 5, 6, 3]
list2 = [16, 3.5, 6]
print(series_resistance(list1))
print(series_resistance(list2))
