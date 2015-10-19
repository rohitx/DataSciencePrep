def only_sorted(L):
    '''
    INPUT: list of list of integers
    OUTPUT: list of list of integers
    
    Use filter to return only the lists from L that are in sorted order.
    Hint: the all function may come in handy.
    
    Example:
    >>> only_sorted([[3, 4, 5], [4, 3, 5], [5, 6, 3], [5, 6, 7]])
    [[3, 4, 5], [5, 6, 7]]
    '''
    return filter(lambda x: x == sorted(x), L)

if __name__ == '__main__':
    L = [[3, 4, 5], [4, 3, 5], [5, 6, 3], [5, 6, 7]]
    print only_sorted(L)