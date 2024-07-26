def sum_two_smallest_numbers(numbers):
    first_smallest = min(numbers)
    numbers.remove(first_smallest)
    second_smallest = min(numbers)
    return first_smallest + second_smallest
print(sum_two_smallest_numbers([12, 2, 34, 91, 1231, 4]))

# SOLUCION MEJOR
# def sum_two_smallest_numbers(numbers):
#     return sum(sorted(numbers)[:2])