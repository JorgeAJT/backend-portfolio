def accum(string):
    new_string = []
    counter = 1
    for i in string:
        if counter == 1:
            new_string.append(i.upper() + "-")
            counter += 1
        elif counter == len(string):
            new_string.append(i.upper() + (i * (counter - 1)))
        else:
            new_string.append(i.upper() + (i * (counter - 1)) + "-")
            counter += 1
    return "".join(new_string)

print(accum("paco"))

