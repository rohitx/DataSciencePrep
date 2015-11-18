'''
Using the Python language, have the function LetterCountI(str) take the str parameter being passed and return the first word with the greatest number of repeated letters. For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. If there are no words with repeating letters return -1. Words will be separated by spaces.
'''
def LetterCountI(string):
    letters = {}
    words = string.split(" ")
    for word in words:
        d = {}
        for l in word:
            if l not in d:
                d[l] = 1
            else:
                d[l] += 1
        letters[word] = d
    return letters

# keep this function call here
# to see how to enter arguments in Python scroll down
print LetterCountI("Today, is the greatest day ever!")