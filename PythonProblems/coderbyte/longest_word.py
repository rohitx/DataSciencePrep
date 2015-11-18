'''
Using the Python language, have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.
'''
def LongestWord(sen):
    d = {}
    words = sen.split(" ")
    for word in words:
        word = word.replace("&","").replace("!","").replace("*","").replace("?","").replace("#","").replace("#","").replace("$","").replace("%","")
        d[word] = len(word)
    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return sorted_d

# keep this function call here
# to see how to enter arguments in Python scroll down
print LongestWord( "hello world")