def square_digits(num):
    str_num = str(num)
    square_num = "".join([str(int(elem)**2) for elem in str_num])
    return int(square_num)
print(square_digits(103))