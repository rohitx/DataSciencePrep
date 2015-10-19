import itertools

def combinations(alphabet, n):
    '''
    INPUT: string, integer
    OUTPUT: list of strings

    Use itertools.combinations to return all the combinations of letters in
    alphabet with length at most n.

    Example:
    >>> combinations('abc', 2)
    ['a', 'b', 'c', 'ab', 'ac', 'bc']
    '''
    comb1 = [comb1[0] for comb1 in itertools.combinations(alphabet, 1)]
    comb2 = [comb2[0]+comb2[1] for comb2 in itertools.combinations(alphabet, n)]
    return comb1 + comb2
if __name__ == '__main__':
    print combinations('abc', 2)
