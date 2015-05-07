def main():
    import math
    a, b, c = input("Enter three sides of the triangle separated by commas: ")
    s = (a + b + c) / 2
    sp = s * (s - a) * (s - b) * (s - c)
    if s < 0:
        print "S is negative"
        break
    elif sp < 0:
        print "The product is negative"
    A = math.sqrt(sp)
    print "The area of the triangle is: ", A
main()
