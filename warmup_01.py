

def count_vowels(phrase):
    count = 0
    phrase = phrase.lower()
    for char in phrase:
        if char in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

print(count_vowels("Celebration")) # ➞ 5
print(count_vowels("Palm")) # ➞ 1
print(count_vowels("Prediction")) # ➞ 4