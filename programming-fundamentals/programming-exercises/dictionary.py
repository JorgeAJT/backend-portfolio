
dictionary = {
    "name": "Rick",
    "age": "1000",
    "power": "Infinite",
    "purpose": "Pass the butter"
}

def change_dictionary(dictionary, name, age, power):

    dictionary["name"] = name
    dictionary["age"] = age
    dictionary["power"] = power
    return dictionary
print(change_dictionary(dictionary, "Robot", "Unknow", "1"))


str