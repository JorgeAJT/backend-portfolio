import math

def square_number(number):
    if number < 0:
        return False
    result = math.sqrt(number)
    result_int = int(result)
    if result - result_int == 0:
        return True
    else:
        return False
print(square_number(-1))