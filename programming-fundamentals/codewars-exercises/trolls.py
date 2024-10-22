# METHOD 1
def delete_vowels_long(string):
    vowels = "aeiou"
    reverse_new_str = ""
    for i in string:
        if i.lower() not in vowels:
            reverse_new_str = i + reverse_new_str
    new_str = ""
    for j in reverse_new_str:
        new_str = j + new_str
    return new_str

print(delete_vowels_long("holidays I need"))

# METHOD 2
def delete_vowels_short(string):
    vowels = "aeiou"
    no_vowel_list = [char for char in string if char.lower() not in vowels]
    no_vowel = "".join(no_vowel_list)
    return no_vowel

print(delete_vowels_short("This website is for losers LOL!"))

# METHOD 3 (MAP)
string = "Today I ate ramen, it was delicious!"
vowels = "aeiou"
no_vowel = map(lambda letter: letter if letter not in vowels else "", string)
no_vowel_list = "".join(no_vowel)
print(no_vowel_list)

# METHOD 4 (FILTER)
string = "Today I ate ramen, it was delicious!"
vowels2 = "aeiou"
no_vowel = filter(lambda letter: (letter not in vowels2), string)
no_vowel_str = "".join(no_vowel)
print(no_vowel_str)

# METHOD 4 (REPLACE())
def delete_vowels_replace(string):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        string = string.replace(vowel, "")
    return string

print(delete_vowels_replace("I want a fucking good job right now, God"))