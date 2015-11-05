'''
You are given a string 'S' and a character 't'. Print out the position of the
rightmost occurrence of 't' (case matters) in 'S' or -1 if there is none.
The position to be printed out is zero based.

INPUT:
Hello World,r
Hello CodeEval,E

OUTPUT:
8
10

Do NOT print out empty lines
'''

with open('rightmost_char.txt', 'r') as f:
    data = f.readlines()

for d in data:
    stripped = d.strip().split(",")
    try:
        print stripped[0].rfind(stripped[1])
    except Exception:
        print -1
