'''
Using the Python language, have the function ABCheck(str) take the str parameter being passed and return the string true if the characters a and b are separated by exactly 3 places anywhere in the string at least once (ie. "lane borrowed" would result in true because there is exactly three characters between a and b). Otherwise return the string false.
'''
def ABCheck(str):
    string = str
    countA = 0
    countB = 0
    for i, l in enumerate(string):
        if l.lower() == 'a':
            countA = i
        elif l.lower() == 'b':
            countB = i
    print countA, countB
    if abs(countB - countA) == 4:
        return 'true'
    else:
        return 'false'
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ABCheck( "after badly")