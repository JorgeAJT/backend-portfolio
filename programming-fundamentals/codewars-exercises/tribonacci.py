

def tribonacci(signature, n):
    if n <=0 :
        return []
    elif 0 < n < 4:
        del signature[n:]
        return signature
    for i in range(n-3):
        new_num = signature[i] + signature[i+1] + signature[i+2]
        signature.append(new_num)
    return signature

print(tribonacci([1,2,3], 4))