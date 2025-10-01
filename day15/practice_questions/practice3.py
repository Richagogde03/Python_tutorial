import re
# grocery store price
# You are given a list of strings consisting of grocery items, with prices in
# parentheses. Return a
# list of prices in float format.

# hard


def get_prices(list1):
    convert_string = str(list1)
    text = r'[0-9]*\.[0-9]{2}'
    match_prices = re.findall(text, convert_string)
    result = []

    for i in match_prices:
        result.append(float(i))

    print(result)


get_prices(["salad ($4.99)"])
get_prices([
  "artichokes ($1.99)",
  "rotiserrie chicken ($5.99)",
  "gum ($0.75)"
])
