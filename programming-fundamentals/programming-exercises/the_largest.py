def largest_element(string, integer):
    if len(string) > len(str(integer)):
        return "The name is larger"
    else:
        return "The number is larger"


print(largest_element("paco", 222333))
