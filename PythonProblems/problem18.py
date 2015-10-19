def sort_by_ratio(L):
    '''
    INPUT: list of 2-tuples of integers
    OUTPUT: None
    
    Sort the list L by the ratio of the elements in the 2-tuples.
    For example, (1, 3) < (2, 4) since 1/3 < 2/4.
    Use the key parameter in the sort method.
    
    Example:
    >>> L = [(2, 4), (8, 5), (1, 3), (9, 4), (3, 5)]
    >>> sort_by_ratio(L)
    >>> L
    [(1, 3), (2, 4), (3, 5), (8, 5), (9, 4)]
    '''
    return L.sort()
