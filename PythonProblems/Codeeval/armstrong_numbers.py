'''
An Armstrong number is an n-digit number that is equal to the sum of the n'th
powers of its digits. Determine if the input numbers are Armstrong numbers.

For example:
An Armstrong number of three digits is an integer such that the sum of the cubes
of its digits is equal to the number itself. For example, 371 is an Armstrong
number since 3**3 + 7**3 + 1**3 = 371.

Your program should accept as its first argument a path to a filename.
Each line in this file has a positive integer. E.g.

INPUT

6
153
351

OUTPUT

True
True
False
'''
def armstrong_number(number):
    str_num = str(number)
    length = len(str_num)
    sum_num = sum([int(n) ** length for n in str_num])
    if str(sum_num) == str_num:
        return True
    else:
        return False

if __name__ == '__main__':
    print armstrong_number(153)