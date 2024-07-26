def even_index(names):
    return [item for index, item in enumerate(names) if index % 2 == 0]

def even_index_loop(names):
    even_names = []
    for index, item in enumerate(names):
        if index % 2 == 0:
            even_names.append(item)
    return even_names

print(even_index_loop(["paco", "daniela", "pedro", "jorge"]))
