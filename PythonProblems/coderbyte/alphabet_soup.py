'''
Using the Python language, have the function AlphabetSoup(str) take the str string parameter being passed and return the string with the letters in alphabetical order (ie. hello becomes ehllo). Assume numbers and punctuation symbols will not be included in the string.
'''
def AlphabetSoup(str):
    string = str
    sorted_string = sorted(string)
    word = "".join([w for w in sorted_string])
    return word

# keep this function call here
# to see how to enter arguments in Python scroll down
print AlphabetSoup("hooplah")