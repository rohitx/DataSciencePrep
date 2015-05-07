"""
avg2.py

A simple program to average two exam scores
Illustrates use of multiple input

"""


def main():
    print "This program computes the average of three exam scores."

    score1, score2, score3 = input("Enter three scores separated by a comma: ")
    average = (score1 + score2 + score3) / 3.0

    print "The average of the scores is: ", average

main()
