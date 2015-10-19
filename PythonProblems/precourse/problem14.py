def alternate(L):
    '''
    INPUT: list
    OUTPUT: list
    
    Use list slicing to return a list containing all the odd indexed elements
    followed by all the even indexed elements.
    
    Example:
    >>> alternate(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    ['b', 'd', 'f', 'a', 'c', 'e', 'g']
    '''
    # First get the even index values
    # Get the odd index values
    # Add the two lists together
    return L[1::2]+L[::2]

if __name__ == '__main__':
    L = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print alternate(L)