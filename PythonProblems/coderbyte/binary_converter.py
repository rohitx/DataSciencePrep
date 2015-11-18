'''
Using the Python language, have the function BinaryConverter(str) return the decimal form of the binary value. For example: if 101 is passed return 5, or if 1000 is passed return 8.
'''
def BinaryConverter(string):
    values = [2**i for i in xrange(len(string))]
    nums = [int(l) for l in string]
    values = sorted(values, reverse=True)
    print values
    print nums
    return sum([values[i]*nums[i] for i in xrange(len(values))])


# keep this function call here  
# to see how to enter arguments in Python scroll down
print BinaryConverter('100101')