def optimizing_list(list_of_dicts):
    new_dict = {
        "181": [],
        "182": [],
        "183": []
    }
    for user in list_of_dicts:
        key = "".join(user.keys())
        value = list(user.values())
        new_dict[key[-3:]].append(value[0])

    return new_dict


result = optimizing_list([
    {"nombre181": "David"},
    {"nombre182": "Jorge"},
    {"nombre183": "Dani"},
    {"edad181": 25},
    {"edad182": 34},
    {"edad183": 28}
])
print(result)


    
"""
x = [
    {"nombre181": "David"},
    {"nombre182": "Jorge"},
    {"nombre183": "Dani"},
    {"edad181": 25},
    {"edad182": 34},
    {"edad183": 28}
]

y = {
    "181": [],
    "182": [],
    "183": []
}

# resultado final
z = {
    "181": ["David", 25]
    # ... etc
}
"""
