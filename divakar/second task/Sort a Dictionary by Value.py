def sort_by_value(data):
    return dict(sorted(data.items(), key=lambda x: x[1]))


data = {"John": 85, "David": 72, "Alex": 95, "Sam": 68}

result = sort_by_value(data)

print(result)