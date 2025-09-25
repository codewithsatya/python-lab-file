
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Get the view object
dict_items = my_dict.items()
print(dict_items)

# Iterate through the key-value pairs
for key, value in dict_items:
    print("Key: {key}, Value: {value}")

# Demonstrate dynamic update
my_dict["occupation"] = "Engineer"
print(dict_items) 

