# Calculate the Total Price of Groceries
# medium

def get_total_price(list1):
    ans = 0
    for i in range(len(list1)):
        temp = 1
        for value in list1[i].values():
            if isinstance(value, str):
                continue
            else:
                temp *= value
        ans += temp
    ans = round(ans, 1)

    if ans % 1 == 0:
        return int(ans)

    return ans


print(get_total_price([
  {"product": "Milk", "quantity": 1, "price": 1.50}
]))
print(get_total_price([
  {"product": "Milk", "quantity": 1, "price": 1.50},
  {"product": "Cereals", "quantity": 1, "price": 2.50}
]))
print(get_total_price([
  {"product": "Milk", "quantity": 3, "price": 1.50}
]))
print(get_total_price([
  {"product": "Milk", "quantity": 1, "price": 1.50},
  {"product": "Eggs", "quantity": 12, "price": 0.10},
  {"product": "Bread", "quantity": 2, "price": 1.60},
  {"product": "Cheese", "quantity": 1, "price": 4.50}
]))
print(get_total_price([
  {"product": "Chocolate", "quantity": 1, "price": 0.10},
  {"product": "Lollipop", "quantity": 1, "price": 0.20}
]))
