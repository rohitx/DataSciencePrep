'''
Using the Python language, have the function LetterCapitalize(str)
take the str parameter being passed and capitalize the first letter
of each word. Words will be separated by only one space.
'''

def LetterCapitalize(str):
    s = str
    words = s.split(" ")
    capWords = " ".join([word[0].upper()+word[1:] for word in words])
    return capWords

# keep this function call here
# to see how to enter arguments in Python scroll down
print LetterCapitalize("i ran there")