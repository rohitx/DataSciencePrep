'''
Using the Python language, have the function WordCount(str) take the str string parameter being passed and return the number of words the string contains (ie. "Never eat shredded wheat" would return 4). Words will be separated by single spaces.
'''
def WordCount(str):
    string = str
    words = string.split(" ")
    return len(words)

# keep this function call here  
# to see how to enter arguments in Python scroll down
print WordCount("Argument goes here")