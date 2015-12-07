'''
Given a list of numbers and a positive integer k, reverse the elements of the list, k items at a time. If the number of elements is not a multiple of k, then the remaining items in the end should be left as is.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains a list of numbers and the number k, separated by a semicolon. The list of numbers are comma delimited. E.g.

1,2,3,4,5;2
1,2,3,4,5;3
OUTPUT SAMPLE:

Print out the new comma separated list of numbers obtained after reversing. E.g.

2,1,4,3,5
3,2,1,4,5
'''

def reverse_group(lst, num):
    interval = num
    last = (len(lst) - (len(lst) % interval)) - 1
    print last
    if interval != 1:
        for i in xrange(0, last, interval):
            print i
            lst[i:i + interval] = lst[i:i + interval][::-1]

    return lst






if __name__ == '__main__':
    print reverse_group([1,2,3,4,5], 2)