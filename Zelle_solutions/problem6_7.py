def nFibonacci(number):
    a = 0
    b = 1
    count = 0
    while count < number:
        c = b
        a, b = b, a + b
        count += 1
    return c


print nFibonacci(7)