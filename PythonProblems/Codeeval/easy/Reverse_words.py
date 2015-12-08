'''
Given numbers x and n, where n is a power of 2, print out the smallest multiple of n which is greater than or equal to x. Do not use division or modulo operator.

INPUT SAMPLE:

The first argument will be a path to a filename containing a comma separated list of two integers, one list per line. E.g.

13,8
17,16

OUTPUT SAMPLE:

Print to stdout, the smallest multiple of n which is greater than or equal to x, one per line. E.g.

16
32
'''
def multiples_of_number(filename):
    with open(filename,'r') as f:
        data = f.readlines()

    for line in data:
        line = line.strip().split(",")
        x = line[0]
        n = line[1]
        
