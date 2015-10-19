def is_palindrome(string):
    '''
    INPUT: string
    OUTPUT: boolean

    Return whether the given string is the same forwards and backwards.

    Example:
    >>> is_palindrome("rats live on no evil star")
    True
    '''
    # Check whether each index value of the string match going
    # forward and backwards
    if string == string[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    print is_palindrome("rats live on no evil star")
    print is_palindrome("Alexis is a naughty girl")