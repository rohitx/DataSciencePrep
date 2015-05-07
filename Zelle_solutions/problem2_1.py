"""A user-friendly program should print an introduction that tells the user
what the program does. Modify the program (Section 2.2) to print an
introduction."""


def main():
    print "This program converts the temperature from degrees\
 Centigrade to degrees Fahrenheit"
    celsius = input("What is the Celsius temperature")
    fahrenheit = (9.0 / 5.0) * celsius + 32
    print "The temperature is ", fahrenheit, "degrees Fahrenheit"

main()
