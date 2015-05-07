def main():
    import math
    num = input("Number of terms to sum: ")
    count = 0
    sum = 0
    n = 0
    while count < num:
        sum = sum + 4 * (1./(2 * n + 1)) * (-1)**n
        count += 1
        n += 1
    print sum
    diff = (math.pi - sum) * 100
    print "This value is different from pi by: ", diff, "percent"


main()
