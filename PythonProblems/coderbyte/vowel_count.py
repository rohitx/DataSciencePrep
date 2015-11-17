'''
Using the Python language, have the function VowelCount(str) take the str
string parameter being passed and return the number of vowels the string
contains (ie. "All cows eat grass" would return 5). Do not count y as a vowel
for this challenge.
'''
def VowelCount(str):
    string = str
    vowel = ['a','e','i','o','u']
    total = sum([1 for s in string if s.lower() in vowel])
    return total

# keep this function call here  
# to see how to enter arguments in Python scroll down
print VowelCount("Argument goes here")