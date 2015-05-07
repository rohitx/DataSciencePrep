def main():
    import math
    x1, x2 = input("Enter two values of x separated by a comma: ")
    y1, y2 = input("Enter two values of y separated by a comma: ")
    distance = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
    print "The slope of the line is: ", distance

main()
