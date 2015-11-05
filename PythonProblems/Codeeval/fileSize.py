import os
def filesize(filename):
    statsinfo = os.stat(filename)
    size = statsinfo.st_size
    return size


if __name__ == '__main__':
    print filesize('fizz_buzz.txt')
