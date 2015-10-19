def word_lengths1(phrase):
    '''
    INPUT: string
    OUTPUT: list of integers
    Use list comprehension to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.
    Example:
    >>> word_lengths1("Welcome to Zipfian Academy!")
    [7, 2, 7, 8]
    '''
    # I will find the length of each of the words through
    # list comprehension
    words = phrase.split(" ")
    return [len(word) for word in words]

if __name__ == '__main__':
    M = "Welcome to Zipfian Academy!"
    print word_lengths1(M)