def anti_vowel(text):
    return "".join([letter for letter in text if letter.lower() not in 'aeiou'])

print anti_vowel('Hey You!')