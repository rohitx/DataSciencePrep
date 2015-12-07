def fizzbuzz(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    for line in data:
        info = line.split(" ")
        if len(info) == 3:
            x = int(info[0])
            y = int(info[1])
            n = int(info[2])
        else:
            return 'File not in right order!'
        result = []
        for num in xrange(1,n+1):
            if num % x ==0 and num % y == 0:
                result.append('FB')
            elif num % x == 0:
                result.append('F')
            elif num % y == 0:
                result.append('B')
            else:
                result.append(num)
    return result

if __name__ == '__main__':
    print fizzbuzz('fizz_buzz.txt')