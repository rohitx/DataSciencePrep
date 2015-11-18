'''
Using the Python language, have the function ArrayAdditionI(arr) take the array of numbers stored in arr and return the string true if any combination of numbers in the array can be added up to equal the largest number in the array, otherwise return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all the same elements, and may contain negative numbers.
'''
from itertools import combinations
def ArrayAdditionI(arr):
    arr_sort = sorted(arr)
    sum_val = sum(arr[:-1])
    largest = arr_sort[-1]
    if sum_val < largest:
        return 'false'
    for i in xrange(2,len(arr_sort)):
        sums = [sum(c) for c in combinations(arr_sort,i)]
        if largest in sums:
            return 'true'



# keep this function call here
# to see how to enter arguments in Python scroll down
print ArrayAdditionI([10,20,30,60,100])

