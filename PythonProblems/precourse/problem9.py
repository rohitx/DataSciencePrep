def word_lengths2(phrase):
    '''
    INPUT: string
    OUTPUT: list of integers
    Use map to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.
    '''
    # I will make use of the lambda function to compute the
    # length of the words
    # first I will break the string into words
    words = phrase.split(" ")
    return map(lambda x: len(x), words)

if __name__ == '__main__':
    M = "Welcome to Zipfian Academy!"
    print word_lengths2(M)