import pickle

# data = {'name': 'John', 'age': 30, 'city': 'New York'}
family_tree = {
    "child1": {
        "name": 'x',
        'age': 12
    },
    "child2": {
        "name": "y",
        'age': 15
    },
    "child3": {
        "name": 'z',
        'age': 20
    }
}
# pickling
with open('family_tree.pickle', 'wb') as f:
    pickle.dump(family_tree, f)

# unpickling
with open('family_tree.pickle', 'rb') as f:
    family_tree_data = pickle.load(f)

print(family_tree_data)
