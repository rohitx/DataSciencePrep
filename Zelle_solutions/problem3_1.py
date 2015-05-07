def main():
    import math
    radius = input("Please enter a radius: ")
    volume = (4/3.) * math.pi * radius ** 3
    surface = 4 * math.pi * radius ** 2
    print "The volume of the sphere is: ", volume
    print "The surface of the sphere is: ", surface

main()
