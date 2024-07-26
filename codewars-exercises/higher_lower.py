def high_and_low(string_numbers):
    number_list = []
    single_char = ""
    for char in string_numbers:
        if char != " ":
            single_char += char
        else:
            number_list.append(int(single_char))
            single_char = ""
    if single_char:
        number_list.append(int(single_char))
    max_number = max(number_list)
    min_number = min(number_list)
    max_min_string = " ".join([str(max_number), str(min_number)])
    return max_min_string

print(high_and_low("2 42 3 0 -1 -9"))

# def high_and_low(numbers): #z.
#     nn = [int(s) for s in numbers.split(" ")]
#     print(nn)
#     return "%i %i" % (max(nn),min(nn))
#
# print(high_and_low("2 42 3 0 -1 -9"))