def make_negative(number):
    if number <= 0:
        return number
    else:
        number = number * -1
        return number

print(make_negative((5)))
print(type(make_negative((5))))
print(make_negative((-4)))
print(make_negative((0)))
print(isinstance(make_negative(5), int))

# isinstance(variable, tipo) ===> false / true

