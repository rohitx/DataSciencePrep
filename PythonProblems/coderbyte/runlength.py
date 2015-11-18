'''
Using the Python language, have the function RunLength(str) take the str parameter being passed and return a compressed version of the string using the Run-length encoding algorithm. This algorithm works by taking the occurrence of each repeating character and outputting that number along with a single character of the repeating sequence. For example: "wwwggopp" would return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbols.
'''
def RunLength(string):
    d = {}
    unique_val = []
    for l in string:
        if l not in d:
            d[l] = 1
            unique_val.append(l)
        else:
            d[l] += 1
    word = "".join([str(d[l])+l for l in unique_val])
    return word

        #word.append(letter+str(number))
    #print word
# keep this function call here
# to see how to enter arguments in Python scroll down
print RunLength("wwwggopp")