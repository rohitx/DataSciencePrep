'''
Using the Python language, have the function NumberSearch(str) take the str parameter, search for all the numbers in the string, add them together, then return that final number. For example: if str is "88Hello 3World!" the output should be 91. You will have to differentiate between single digit numbers and multiple digit numbers like in the example above. So "55Hello" and "5Hello 5" should return two different answers. Each string will contain at least one letter or symbol.
'''
def NumberAddition(string):
    addition = []
    if string[0].isdigit():
        addition.append(string[0])
    for i in xrange(1,len(string)):
        previous = string[i-1]
        current = string[i]
        if previous.isdigit() and current.isdigit():
            addition.append(previous+current)
        elif current.isdigit():
            addition.append(current)
    print addition
    total = sum([int(v) for v in addition])
    return total



# keep this function call here
# to see how to enter arguments in Python scroll down
#print NumberAddition('88Hello 3World!!')
#print NumberAddition('55Hello')
print NumberAddition("T1wo Ho33uses")
print NumberAddition("1 1 1 7 yes")
print NumberAddition("7Yes9 Sir2")
print NumberAddition("Won90 8")