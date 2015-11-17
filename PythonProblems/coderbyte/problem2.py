'''
Using the Python language, have the function LetterChanges(str)
take the str parameter being passed and modify it using the following
algorithm. Replace every letter in the string with the letter following
it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every
vowel in this new string (a, e, i, o, u) and finally return this modified
string.
'''
def LetterChanges(str):
  alphabet = {'a': 'b',
              'b':'c',
              'c':'d',
              'd':'e',
              'e':'f',
              'f':'g',
              'g':'h',
              'h':'i',
              'i':'j',
              'j':'k',
              'k':'l',
              'l':'m',
              'm':'n',
              'n':'o',
              'o':'p',
              'p':'q',
              'q':'r',
              'r':'s',
              's':'t',
              't':'u',
              'u':'v',
              'v':'w',
              'w':'x',
              'x':'y',
              'y':'z',
              'z':'a'}
  vowels = ['a','e','i','o','u']
  word = []
  string = str
  for s in string:
    s = s.lower()
    if s in alphabet and alphabet[s] in vowels:
      word.append(alphabet[s].upper())
    elif s in alphabet:
      word.append(alphabet[s])
    else:
        word.append(s)
  final_word = "".join(word)
  return final_word

# keep this function call here
# to see how to enter arguments in Python scroll down
print LetterChanges("Argument goes here")