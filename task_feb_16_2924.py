# Ordered Dictionary

"""

An OrderedDict is a dictionary subclass that maintains the order in which items are inserted. 
Unlike a regular dictionary, which does not guarantee any specific order of items, an OrderedDict keeps track of the order in which key-value pairs are added.

"""
from collections import OrderedDict

od = OrderedDict()
od["a"] = 10
od["b"] = 500
od["c"] = 200
od["d"] = 2
od["e"] = 30
od["f"] = 80

print(od)


# Other ways to make an OrderedDict

# Passing a List of Tuples:

items = [('a', 10), ('b', 500), ('c', 200), ('d', 2), ('e', 30), ('f', 80)]
od = OrderedDict(items)
print(od)

# Using a Dictionary:

my_dict = {'a': 10, 'b': 500, 'c': 200, 'd': 2, 'e': 30, 'f': 80}
od = OrderedDict(my_dict)
print(od)

# iterate through a dictionary in Python

my_dict = {'a': 10, 'b': 500, 'c': 200, 'd': 2, 'e': 30, 'f': 80}

# Iterating through keys
for key in my_dict:
    print(key)

# Iterating through values
for value in my_dict.values():
    print(value)

# Iterating through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")


# --------------- For searching in a dictionary using the in keyword, you can check if a key exists in the dictionary. 

my_dict = {'a': 10, 'b': 500, 'c': 200, 'd': 2, 'e': 30, 'f': 80}

# Searching for a key
key_to_search = 'c'
if key_to_search in my_dict:
    print(f"{key_to_search} is in the dictionary. Its value is {my_dict[key_to_search]}")
else:
    print(f"{key_to_search} is not in the dictionary")
