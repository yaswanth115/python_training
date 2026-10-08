def convert_to_dictionary(keys, values):
    dictionary = {}

    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]

    return dictionary


keys = ["name", "age", "city"]
values = ["John", 25, "Hyderabad"]

result = convert_to_dictionary(keys, values)

print(result)