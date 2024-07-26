# EXERCISE 1

def divisible_three(number):
    if number % 3 == 0:
        return print("Number divisible by 3")
    else:
       return print("Number not divisible by 3")

x1 = int(input("Please, enter a number: "))
divisible_three(x1)

# EXERCISE 2
def even_odd(number):
    if number % 2 == 0:
        return print("Number is even")
    else:
       return print("Number is odd")

x2 = int(input("Please, enter a number: "))
even_odd(x2)

# EXERCISE 3
def older(number):
    if number > 18:
        return print("Old enough")
    else:
       return print("Too young")

x3 = int(input("Please, enter your age: "))
older(x3)

# EXERCISE 4
def same_name(name):
    if name.lower() == "jorge":
        return print("You have the same name as me!")

x4 = input("Please, enter your name: ")
same_name(x4)

# EXERCISE 5
def leap_year(year):
    if year % 4 == 0:
        return print(f"The year {year} is leap")
    else:
       return print(f"The year {year} is NOT leap")

leap_year(2020)
leap_year(2021)

# SIMPLE EXERCISE
def int_to_str(number):
    string = str(number)
    return string
print(int_to_str(23344)) # "23344"
print(isinstance(int_to_str(23344), str)) # True