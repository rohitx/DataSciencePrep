'''
Using the Python language, have the function DivisionStringified(num1,num2) take both parameters being passed, divide num1 by num2, and return the result as a string with properly formatted commas. If an answer is only 3 digits long, return the number with no commas (ie. 2 / 3 should output "1"). For example: if num1 is 123456789 and num2 is 10000 the output should be "12,346".
'''
import math
def DivisionStringified(num1,num2):
    if num1/num2 > 9999:
        result ='{:5,.0f}'.format((num1) / (num2))
        return result
    else:
        return str((num1/num2))





# keep this function call here
# to see how to enter arguments in Python scroll down
print DivisionStringified(123456789, 10000)
print DivisionStringified(5, 2)
print DivisionStringified(6874, 67)
print DivisionStringified(503394930, 20)