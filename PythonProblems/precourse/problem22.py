def transpose(mat):
    '''
    INPUT: 2 dimensional list of integers
    OUTPUT: 2 dimensional list of integers

    Return the transpose of the matrix. You may assume that the matrix is not
    empty. You can do this using a double for loop in a list comprehension.
    There is also a solution using zip.
    '''
    return [a for a in zip(mat[0], mat[1])]

if __name__ == '__main__':
    M = [[2,4],[3,7]]
    print transpose(M)
