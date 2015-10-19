"""A median is a numerical value separating the upper half of a sorted array of
numbers from the lower half. In a list where there are an odd number of
entities, the median is the number found in the middle of the array.
If the array contains an even number of entities, then there is no single
middle value, instead the median becomes the average of the two numbers found
in the middle. For this mission, you are given a non-empty array of natural
numbers (X). With it, you must separate the upper half of the numbers from the
lower half and find the median."""


def get_median(data):
    # get the length of data:
    arr_len = len(data)
    # sort the data
    for k in range(1, len(data)):
        cur = data[k]
        j = k
        while j > 0 and data[j-1] > cur:
            data[j] = data[j-1]
            j -= 1
        data[j] = cur
    #print data
    if (arr_len % 2 != 0):
        index = arr_len / 2
        median = data[index]
    else:
        index = arr_len / 2
        median = (data[index] + data[index-1]) / 2.
    return median


data = [1, 2, 3, 4, 5]
data1 = [3, 1, 2, 5, 3]
data2 = [3, 6, 20, 99, 10, 15]
data3 = list(range(1000000))
data4 = [1, 300, 2, 200, 1]
print get_median(data4)