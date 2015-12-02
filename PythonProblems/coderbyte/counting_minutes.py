'''
Using the Python language, have the function CountingMinutesI(str) take the str parameter being passed which will be two times (each properly formatted with a colon and am or pm) separated by a hyphen and return the total number of minutes between the two times. The time will be in a 12 hour clock format. For example: if str is 9:00am-10:00am then the output should be 60. If str is 1:00pm-11:00am the output should be 1320. 
'''
def CountingMinutesI(string):
    times = string.split("-")
    times1 = times[0]
    times2 = times[1]
    hour1 = int((times1.split(":"))[0])
    min1 = int(((times1.split(":"))[1])[:2])
    day1 = times1[-2:]
    # Time 2
    hour2 = int((times2.split(":"))[0])
    min2 = int(((times2.split(":"))[1])[:2])
    day2 = times2[-2:]

    if day2 == 'pm' and day2 < 12:
        hour2 = hour2 + 12
    if day1 == 'pm' and day2 < 12:
        hour1 = hour1 + 12
    print hour1
    #minutes = 0
    if hour1 > hour2 or min1 > min2:
        minutes = (24 - hour1 + hour2) * 60 - min1 - min2
        print 'a'
        return minutes
    else:
        minutes = (hour2 - hour1) * 60
        return minutes




# keep this function call here  
# to see how to enter arguments in Python scroll down
print CountingMinutesI("12:30pm-12:05am")