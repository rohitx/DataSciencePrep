def concatenate(L1, L2, connector=""):
    '''
    INPUT: list of strings, list of strings
    OUTPUT: list of strings

    L1 and L2 have the same length. Use zip and other skills from above to
    return a list of the same length where each value is the two strings from
    L1 and L2 concatenated together with connector between them.

    Example:
    >>> concatenate(["A", "B"], ["b", "b"])
    ['Ab', 'Bb']
    >>> concatenate(["San Francisco", "New York", "Las Vegas", "Los Angeles"], \
                    ["California", "New York", "Nevada", "California"], ", ")
    ['San Francisco, California', 'New York, New York', 'Las Vegas, Nevada',
    'Los Angeles, California']
    '''
    return [word[0]+connector+word[1] for word in zip(L1, L2)]

if __name__ == '__main__':
    L1 = ["San Francisco", "New York", "Las Vegas", "Los Angeles"]
    L2 = ["California", "New York", "Nevada", "California"]
    print concatenate(L1,L2, ", ")