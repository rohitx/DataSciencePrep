
def shuffle(L):
    '''
    INPUT: list
    OUTPUT: list

    Return the result of a "perfect" shuffle. You may assume that L has even
    length. You should return the result of splitting L in half and alternating
    taking an element from each.

    Example:
    >>> shuffle([1, 2, 3, 4, 5, 6])
    [1, 4, 2, 5, 3, 6]
    '''
    shuffle_lst = []
    m = len(L) / 2
    for i in xrange(len(L)):
        if i+(m+1) > len(L):
            break
        elif L[i] not in shuffle_lst:
            shuffle_lst.append(L[i])
            shuffle_lst.append(L[i+m])
    return shuffle_lst


if __name__ == '__main__':
    print shuffle([1, 2, 3, 4, 5, 6, 7, 8])
