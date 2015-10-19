def invert_list(L):
    '''
    INPUT: list
    OUTPUT: dictionary
    
    Use enumerate and other skills from above to return a dictionary which has
    the values of the list as keys and the index as the value. You may assume
    that a value will only appear once in the given list.
    
    Example:
    >>> invert_list(['a', 'b', 'c', 'd'])
    {'a': 0, 'c': 2, 'b': 1, 'd': 3}
    '''
    return {val: i for i, val in enumerate(L)}

if __name__ == '__main__':
    L = ['a', 'b', 'c', 'd']
    print invert_list(L)