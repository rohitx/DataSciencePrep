'''
Using the Python language, have the function TimeConvert(num) take the num parameter being passed and return the number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3). Separate the number of hours and minutes with a colon.
'''
def TimeConvert(num):
    if num > 0:
        hours = num / 60
        minutes = num - hours * 60
        return str(hours)+":"+str(minutes)
# keep this function call here
# to see how to enter arguments in Python scroll down
print TimeConvert(61)
