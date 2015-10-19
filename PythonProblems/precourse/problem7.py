def average_rows2(mat):
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: list of floats
    Use map to take the average of each row in the matrix and
    return it as a list.
    '''
    return map(lambda x: sum(x)/float(len(x)), mat)


if __name__ == '__main__':
    M = [[4, 5, 2, 8], [3, 9, 6, 7]]
    print average_rows2(M)