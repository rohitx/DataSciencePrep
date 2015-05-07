def main():
    import math
    diameter = input("Enter diameter of a pizza: ")
    price = input("Enter price of a pizza: ")
    A = math.pi * (diameter / 2.) ** 2
    cost_per_square_inch = price / A
    print "The price per square inch of a pizza is: ", cost_per_square_inch

main()
