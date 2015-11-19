'''
Using the Python language, have the function MeanMode(arr) take the array of numbers stored in arr and return 1 if the mode equals the mean, 0 if they don't equal each other (ie. [5, 3, 3, 3, 1] should return 1 because the mode (3) equals the mean (3)). The array will not be empty, will only contain positive integers, and will not contain more than one mode.
'''
def MeanMode(arr):
    mean = sum(arr) / len(arr)
    d = {}
    for val in arr:
        if val not in d:
            d[val] = 1
        else:
            d[val] += 1
    sorted_d = sorted(d.items(), key=lambda x: x[1])
    mode = sorted_d[-1][0]
    if mean == mode:
        return 1
    else:
        return 0

# keep this function call here
# to see how to enter arguments in Python scroll down
print MeanMode([5, 3, 3, 3, 1])
print MeanMode([4, 4, 4, 6, 2])