'''
A sequence of n > 0 integers is called a jolly jumper if the absolute values of the differences between successive elements take on all possible values 1 through n - 1. eg. 
1 4 2 3 
is a jolly jumper, because the absolute differences are 3, 2, and 1, respectively. The definition implies that any sequence of a single integer is a jolly jumper. Write a program to determine whether each of a number of sequences is a jolly jumper. 
INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain an integer n < 3000 followed by n integers representing the sequence. The integers are space delimited.

For example:

4 1 4 2 3
3 7 7 8
9 8 9 7 10 6 12 17 24 38

OUTPUT SAMPLE:

For each line of input generate a line of output saying 'Jolly' or 'Not jolly'.

For example:

Jolly
Not jolly
Not jolly

'''
def jolly_jumper(sequence):
    all_sums = []
    for i in xrange(len(sequence)):
        if  i+1 < len(sequence):
            sums = abs(sequence[i] - sequence[i+1])
            all_sums.append(sums)
    all_sort = sorted(all_sums)
    if all_sort[0] == 1 and all_sort[1] == 2 and all_sort[2] == 3:
        return 'Jolly'
    else:
        return 'Not Jolly'

if __name__ == '__main__':
    print jolly_jumper([4, 1, 4, 2, 3])
    print jolly_jumper([3, 7, 7, 8])
    print jolly_jumper([9, 8, 9, 7, 10, 6, 12, 17, 24, 38])
