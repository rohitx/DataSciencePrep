"""A user-friendly program should print an introduction that tells the user
what the program does. Modify the program (Section 2.2) to print an
introduction."""


def main():
    fahrenheit = input("What is the Fahrenheit temperature: ")
    Celcius = (5.0 / 9.0) * (fahrenheit - 32)
    print "The temperature is ", Celcius, "degrees Celcius"

main()
