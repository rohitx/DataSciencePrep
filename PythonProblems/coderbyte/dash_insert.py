'''
Using the Python language, have the function DashInsert(str) insert dashes ('-') between each two odd numbers in str. For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number.
'''
def DashInsert(string):
    odd = ['1','3','5','7','9']
    numbers = [string[0]]
    for i in xrange(1,len(string)):
        previous = string[i-1]
        current = string[i]
        if previous in odd and current in odd:
            numbers.append("-"+current)
        else:
            numbers.append(current)
    result = "".join([v for v in numbers])
    return result




# keep this function call here  
# to see how to enter arguments in Python scroll down
print DashInsert('454793')
print DashInsert('99946')
print DashInsert('56730')