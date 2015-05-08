def antsong(count):
    print "The ants go marching " + count + " by " + count + ", hurrah! hurrah!"
    print "The ants go marching " + count + " by " + count + ", hurrah! hurrah!"
    print "The ants go marching " + count + " by " + count + ","
    print "The little one stops to suck his thumb,"
    print "And they all go marching down..."
    print "In the ground..."
    print "To get out...."
    print "Of the rain."
    print "Boom! Boom! Boom!"
    return ""

numbers = ["one", "two", "three", "four", "five", "six"]

count = 0
while count < 5:
    print antsong(numbers[count])
    count += 1

