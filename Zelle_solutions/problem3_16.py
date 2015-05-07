def main():
    n = input("Enter the value of n: ")
    count = 0
    a = 0
    b = 1
    while count < n:
        print b
        a, b = b, a
        count += 1
main()
