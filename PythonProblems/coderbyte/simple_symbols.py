'''
Using the Python language, have the function SimpleSymbols(str) take the str
parameter being passed and determine if it is an acceptable sequence by either
returning the string true or false. The str parameter will be composed of +
and = symbols with several letters between them (ie. ++d+===+c++==a) and for
the string to be true each letter must be surrounded by a + symbol. So the
string to the left would be false. The string will not be empty and will have
at least one letter.
'''
def SimpleSymbols(str):
    alphabet = ['a','b','c','d',
                'e','f','g','h',
                'i','j','k','l',
                'm','n','o','p',
                'q','r','s','t',
                'u','v','w','x',
                'y','z']
    string = str
    truth = []
    for i, s in enumerate(string):
        #print i, s
        if s in alphabet:
            if string[0] in alphabet or string[-1] in alphabet:
                return 'False'
            if i >= 1 and i < len(string):
                if string[i-1] == '+' and string[i+1] == '+':
                    truth.append(True)
                else:
                    truth.append(False)
    if False in truth:
        return 'false'
    else:
        return 'true'

# keep this function call here
# to see how to enter arguments in Python scroll down
print SimpleSymbols("b")