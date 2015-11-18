'''
Using the Python language, have the function ExOh(str) take the str parameter being passed and return the string true if there is an equal number of x's and o's, otherwise return the string false. Only these two letters will be entered in the string, no punctuation or numbers. For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.
'''
def ExOh(str):
    string = str
    x_count = 0
    o_count = 0
    for l in string:
        if l == 'x':
            x_count +=1
        elif l == 'o':
            o_count +=1
    if x_count == o_count:
        return 'true'
    else:
        return 'false'

# keep this function call here  
# to see how to enter arguments in Python scroll down
print ExOh("xooxx")
