import json


# writing to a json file(serialization)
# To save Python data (like a dictionary or list) to a JSON file,
# use json.dump().
# data = {
#     "name": "Alice",
#     "age": 30,
#     "isStudent": False,
#     "courses": ["Math", "Science"]
# }
# with open("items.json", 'w') as file:
#     json.dump(data, file, indent=4)


# reading from a json file
# To load JSON data from a file into a Python object, use json.load().
with open("items.json", "r") as file:
    loaded_data = json.load(file)
    print("Loaded data = ", loaded_data)
    print("Name: ", loaded_data['name'])
