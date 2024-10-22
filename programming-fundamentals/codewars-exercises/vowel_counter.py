def get_count(sentence):
    vowels = "aeiou"
    counter = 0
    for char in sentence:
        if char in vowels:
            counter += 1
    return counter
print(get_count("the dog ate my homework"))

