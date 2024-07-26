import math


def cut_string(string):
    return string[:math.floor(len(string)/2)]


print(cut_string("supercalifragilisipiestealidoso"))
