'''
When John was a little kid he didn't have much to do. There was no internet, no Facebook, and no programs to hack on. So he did the only thing he could... he evaluated the beauty of strings in a quest to discover the most beautiful string in the world.

Given a string s, little Johnny defined the beauty of the string as the sum of the beauty of the letters in it. The beauty of each letter is an integer between 1 and 26, inclusive, and no two letters have the same beauty. Johnny doesn't care about whether letters are uppercase or lowercase, so that doesn't affect the beauty of a letter. (Uppercase 'F' is exactly as beautiful as lowercase 'f', for example.)

You're a student writing a report on the youth of this famous hacker. You found the string that Johnny considered most beautiful. What is the maximum possible beauty of this string?

INPUT

ABbCcc
Good luck in the Facebook Hacker Cup this year!
Ignore punctuation, please :)
Sometimes test cases are hard to make up.
So I just go consult Professor Dalves

OUTPUT
152
754
491
729
646

'''

def beauty_string(string):
    alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
                'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
               'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
               'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
               'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
               'Z': 26}
    expressions = ['~!@#$%^&*()_;",']

    total = sum([alphabet[letter.upper()] for letter in string.replace(" ","") if letter not in expressions])
    return total

if __name__ == '__main__':
    print beauty_string('Good luck in the Facebook Hacker Cup this year!')
