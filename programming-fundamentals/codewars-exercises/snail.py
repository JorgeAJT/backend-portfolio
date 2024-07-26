

def snail(array):
    if not array or not array[0]:
        return []
    left, right = 0, len(array) - 1
    top, bottom = 0, len(array) - 1
    snail_array = []
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            snail_array.append(array[top][i])
        top += 1
        for i in range(top, bottom + 1):
            snail_array.append(array[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                snail_array.append(array[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                snail_array.append(array[i][left])
            left += 1
    return snail_array
print(snail([[1,2,3], [8,9,4], [7,6,5]]))
print(snail([[1,2], [8,9]]))
print(snail([[1,2,3,1], [4,5,6,4], [7,8,9,7], [7,8,9,7]]))