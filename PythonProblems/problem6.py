import numpy as np
def average_rows1(mat):
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: list of floats
    Use list comprehension to take the average of each row in the matrix and
    return it as a list.
    Example:
    >>> average_rows1([[4, 5, 2, 8], [3, 9, 6, 7]])
    [4.75, 6.25]
    '''
    # This looks like a list of lists
    # I will use list comprehension to create a new list
    # and compute average for each list. Should I use the in-build
    # average function or create my own? Do both
    #
    # Using in-built function
    return [np.mean(col) for col in mat]
    #
    # Creating from scratch
    #  First compute the sum for each col
    #  Compute the length of each column
    #  Calculate the average
    sums_len = {}
    for col in mat:
        count = 0
        sums = 0
        for element in col:
            sums += element
            count += 1
        sums_len[sums] = count
    print sums_len
    return [total/float(count) for total, count in sums_len.iteritems()]

if __name__ == '__main__':
    M = [[4, 5, 2, 8], [3, 9, 6, 7]]
    print average_rows1(M)