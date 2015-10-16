def even_odd1(L):
    '''
    INPUT: list of integers
    OUTPUT: list of strings
    
    Use list comprehension to return a list of the same length with the strings
    "even" or "odd" depending on whether the element in L is even or odd.
    
    Example:
    >>> even_odd([6, 4, 1, 3, 8, 5])
    ['even', 'even', 'odd', 'odd', 'even', 'odd']
    '''
    # The list comprehension will include an if statement
    # that will determine if the number is even or odd
    # the test to determine the parity of the number is
    # with the modulo operator
    return ['even' if num%2 == 0 else 'odd' for num in L ]

if __name__ == '__main__':
    M = [6, 4, 1, 3, 8, 5]
    print even_odd1(M)