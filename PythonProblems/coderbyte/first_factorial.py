'''
Using the Python language, have the function FirstFactorial(num)
take the num parameter being passed and return the factorial of it
(ie. if num = 4, return (4 * 3 * 2 * 1)). For the test cases, the
range will be between 1 and 18.
'''
def FirstFactorial(num):
    total = 1
    if num > 0:
        for n in xrange(1,num+1):
            total *= n
        return total
    else:
        return 'Not a positive number'

if __name__ == '__main__':
    print FirstFactorial(4)
