'''
Write a program to determine the largest sum of contiguous integers in a list.

INPUT SAMPLE:

The first argument is a path to a filename containing a comma-separated list of integers, one per line.

For example:

-10,2,3,-2,0,5,-15
2,3,-2,-1,10
OUTPUT SAMPLE:

Print to stdout the largest sum. In other words, of all the possible contiguous subarrays for a given array, find the one with the largest sum, and print that sum.

For example:

8
12
'''

def sum_of_integers(filename):
    with open(filename) as f:
        data = f.readlines()
    
    max_val = []
    for d in data:
        for i in xrange(len(d)):
            total = 0
            new_d = d[i+1:]
            for j in xrange(len(new_d)):
                if d[i] != d[j]:
                    if d[i] + new_d[j] > 0:
                        total += new_d[j]
            max_val.append(total)
        print max(max_val)

if __name__ == '__main__':
    print sum_of_integers('sum_of_integers.txt')
