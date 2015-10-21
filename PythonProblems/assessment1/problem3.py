def word_count(filename):
    '''
    INPUT: STRING
    OUTPUT: (INT, INT, INT)

    filename refers to a text file.
    Return a tuple containing these stats for the file in this order:
      1. number of lines
      2. number of words (broken by whitespace)
      3. number of characters
    '''
    lines = open(filename, 'r').readlines()
    num_lines = len(lines)
    all_lines = "".join([line.replace("\n", "") for line in lines])
    words = all_lines.split()
    num_words = len(words)
    num_char = sum([len(word) for word in words])
    return num_lines, num_words, num_char


if __name__ == '__main__':
    print word_count('alice.txt')



