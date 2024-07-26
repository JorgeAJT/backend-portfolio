def solution(number):
    if number < 0:
        return 0
    multiples_list = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            multiples_list.append(i)
    return sum(multiples_list)
print(solution(10))