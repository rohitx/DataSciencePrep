def acronym(phrase):
    '''
    INPUT: string
    OUTPUT: string
    Given a phrase, return the associated acronym by breaking on spaces and
    concatenating the first letters of each word together capitalized.
    Example:
    >>> acronym("zipfian academy")
    'ZA'
    Hint: You can do this on one line using list comprehension and the join
    method. Python has a builtin string method to uppercase strings.
    '''
    return "".join([word[0] for word in phrase.split(" ")])

if __name__ == '__main__':
    print acronym('zipfian academy')
