'''
Input:
Hello World
Hello CodeEval

Output:
World Hello
CodeEval Hello
'''

#Split the string
#Reverse the list
#Join the list

def reverse_words(string):
    words = string.split(" ")
    words.reverse()
    join_words = " ".join([w for w in words])
    return join_words

if __name__ == '__main__':
    print reverse_words('Hello CodeEval')
