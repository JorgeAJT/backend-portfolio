import math

def get_middle(string):
    half_length = len(string)/2
    if len(string) % 2 == 0:
        return string[math.floor(half_length)-1:
                      math.floor(half_length)+1]
    else:
        return string[math.floor(half_length)]

print(get_middle("holapollo"))
print(get_middle("como"))

# variable len