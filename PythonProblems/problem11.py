def even_odd2(L):
    '''
    INPUT: list of integers
    OUTPUT: list of strings
    
    Use map to return a list of the same length with the strings
    "even" or "odd" depending on whether the element in L is even or odd.
    '''
    return map(lambda x: 'odd' if x%2 != 0 else 'even', L)

if __name__ == '__main__':
    M = [6, 4, 1, 3, 8, 5]
    print even_odd2(M)