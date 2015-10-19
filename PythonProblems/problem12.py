def shift_on_character(string, char):
    '''
    INPUT: string, string
    OUTPUT: string
    
    Find the first occurence of the character char and return the string witth
    everything before char moved to the end of the string. If char doesn't
    appear, return the same string.
    
    This function may use more than one line.
    
    Example:
    >>> shift_on_character("zipfian", "f")
    'fianzip'
    '''
    # Find the index of the character
    # Slice the string from this index to the beginning
    # Join the beginning to the end
    index = string.index(char)
    return string[index:] + string[:index]

if __name__ == '__main__':
    print shift_on_character("zipfian", "f")