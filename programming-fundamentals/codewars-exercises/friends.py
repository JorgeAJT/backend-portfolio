def friends(arr):
    return list((filter(lambda friend: len(friend) == 4, arr)))
print(friends(["Paco", "Pancracio", "Edmundo", "Paul", "Iñaqui", "Up"]))