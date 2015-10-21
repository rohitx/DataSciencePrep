def count_characters(string):
    '''
    INPUT: STRING
    OUTPUT: DICT (STRING => INT)

    Return a dictionary which contains a count of the number of times each
    character appears in the string.
    Characters which would have a count of 0 should not need to be included in
    your dictionary.
    '''
    d = {}
    for letter in string:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
    return d


if __name__ == '__main__':
    print count_characters('hello')
