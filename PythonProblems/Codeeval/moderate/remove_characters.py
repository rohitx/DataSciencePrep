'''
The first argument is a path to a file. The file contains the source strings and the characters that need to be scrubbed. Each source string and characters you need to scrub are delimited by comma.

For example:

how are you, abc
hello world, def
OUTPUT SAMPLE:

Print to stdout the scrubbed strings, one per line. Ensure that there are no trailing empty spaces on each line you print.

For example:

how re you
hllo worl
'''

def remove_chars(filename):
    with open(filename) as f:
        data = f.readlines()
    for d in data:
        this_line = d.split(",")
        line = "".join([s for s in this_line[0] if s not in this_line[1]])
        print line


if __name__ == '__main__':
    print remove_chars('remove_characters.txt')
