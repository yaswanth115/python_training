def sort_by_key(data):
    return dict(sorted(data.items()))


data = {"banana": 20, "apple": 10, "orange": 30, "mango": 15}

result = sort_by_key(data)

print(result)