def main():
    import math
    x = input("Find square root of a value: ")
    n = input("Number of times you want to iterate: ")
    guess = x / 2
    count = 0
    while count < n:
        guess = (guess + (x / guess)) / 2.
        count += 1
    print "Square root with Netwon's method: ", guess
    print "Using math library: ", math.sqrt(x)
main()
