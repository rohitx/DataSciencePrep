def filter_words(word_list, letter):
    '''
    INPUT: list of words, string
    OUTPUT: list of words
    Use filter to return the words from word_list which start with letter.
    Example:
    >>> filter_words(["salumeria", "dandelion", "yamo", "doc loi", "rosamunde",
                      "beretta", "ike's", "delfina"], "d")
    ['dandelion', 'doc loi', 'delfina']
    '''
    words = [word for word in word_list if word[0] == letter]
    return words

if __name__ == '__main__':
    print filter_words(["salumeria", "dandelion", "yamo", "doc loi", "rosamunde",
                      "beretta", "ike's", "delfina"], "d")