'''
Your program should accept a path to a file as its first argument. The file contains multiple lines. The first line indicates the number of lines you should output, the other lines are of different length and are presented randomly. You may assume that the input file is formatted correctly and the number in the first line is a valid positive integer.

For example:

2
Hello World
CodeEval
Quick Fox
A
San Francisco
OUTPUT SAMPLE:

Print out the longest lines limited by specified number and sorted by their length in descending order.

For example:

San Francisco
Hello World
'''

def longest_lines(filename):
    with open(filename) as f:
        data = f.readlines()
    num_lines = int(data[0].strip())
    d = {}
    data = data[1:]
    for line in data:
        if line not in d:
            d[line] = len(line.strip())
    sorted_val = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for i in xrange(num_lines):
        print sorted_val[i][0]

if __name__ == '__main__':
    print longest_lines('longest_lines.txt')

