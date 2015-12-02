'''
Using the Python language, have the function SwapCase(str) take the str parameter and swap the case of each character. For example: if str is "Hello World" the output should be hELLO wORLD. Let numbers and symbols stay the way they are.
'''
def SwapCase(string):
    final_string = []
    for letter in string:
        if letter == letter.upper():
            final_string.append(letter.lower())
        else:
            final_string.append(letter.upper())
    result = "".join([l for l in final_string])
    return result



# keep this function call here  
# to see how to enter arguments in Python scroll down
print SwapCase("Sup DUDE!!?")