def count_match_index(L):
    '''
    INTPUT: list of integers
    OUTPUT: integer
    
    Use enumerate and other skills from above to return the count of the number
    of items in the list whose value equals its index.
    
    Example:    
    >>> count_match_index([0, 2, 2, 3, 6, 5])
    4
    '''
    count = 0
    for i, val in enumerate(L):
        if i == val:
            count += 1
    return count



if __name__ == '__main__':
    L = [0, 2, 2, 3, 6, 5]
    print count_match_index(L)