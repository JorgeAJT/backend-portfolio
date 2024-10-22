import math

def persistence(n):
    counter = 0
    while n >= 10:
        n_list = list(str(n))
        for index in range(len(n_list)):
            n_list[index] = int(n_list[index])
        n = math.prod(n_list)
        counter += 1
    return counter
print(persistence(39))