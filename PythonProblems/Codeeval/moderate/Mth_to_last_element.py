'''
Write a program which determines the Mth to the last element in a list.

INPUT SAMPLE:

The first argument is a path to a file. The file contains the series of space delimited characters followed by an integer. The integer represents an index in the list (1-based), one per line.

For example:

a b c d 4
e f g h 2
OUTPUT SAMPLE:

Print to stdout the Mth element from the end of the list, one per line. If the index is larger than the number of elements in the list, ignore that input.

For example:

a
g
'''

def mth_list(filename):
    with open(filename) as f:
        data = f.readlines()
    for d in data:
        d_new = d.strip().split(" ")
        index_val = -1 + -1 * int(d_new[-1])
        print d_new[index_val]
    return None

if __name__ == '__main__':
    print mth_list('Mth_to_last_element.txt')

