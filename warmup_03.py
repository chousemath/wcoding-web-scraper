def replace_vowels(phrase, replacement_character):
    new_phrase = ""
    vowels = ["a", "e", "i", "o", "u"]
    for original_character in phrase:
        if original_character in vowels:
            new_phrase += replacement_character
        else:
            new_phrase += original_character
    return new_phrase


print(replace_vowels("the aardvark", "#"))  # ➞ "th# ##rdv#rk"
print(replace_vowels("minnie mouse", "?"))  # ➞ "m?nn?? m??s?"
print(replace_vowels("shakespeare", "*"))  # ➞ "sh*k*sp**r*"
