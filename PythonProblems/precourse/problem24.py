def intersection_of_sets(list_of_sets):
    '''
    INPUT: list of sets
    OUTPUT: set

    Use reduce to take the intersection of a list of sets.
    Hint: the & operator takes the intersection of two sets.

    Example:
    >>> intersection_of_sets([{1, 2, 3}, {2, 3, 4}, {2, 5}])
    set([2])
    '''
    return set.intersection(*list_of_sets)

if __name__ == '__main__':
    L = [{1, 2, 3}, {2, 3, 4}, {2, 5}]
    print intersection_of_sets(L)