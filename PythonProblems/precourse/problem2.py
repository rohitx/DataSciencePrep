"""
You are given a non-empty list of integers (X). For this task, you should return
a list consisting of only the non-unique elements in this list. To do so you will
need to remove all unique elements (elements which are contained in a given list
only once). When solving this task, do not change the order of the list.
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be
[1, 3, 1, 3].

checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
checkio([1, 2, 3, 4, 5]) == []
checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]

"""

# find unique elements in the list
# Get the indices and remove them from the list
# return the updated list
a = [1, 2, 3, 1, 3]
b = [5, 5, 5, 5, 5]
c = [5, 5, 5, 5, 4]
d = [1, 2, 3, 4, 5]


def find_dup(data):
    if len(list(set(data))) == len(data):
        return []
    new_data = data[:]
    for i in data:
        print i
        if data.count(i) == 1:
            #print i
            new_data.remove(i)
    return new_data

e = [10, 20, 30, 10]
print find_dup(d)


# More elegant solution:

def find_dup2(data):
    return [x for x in data if data.count(x) > 1]



# find the unique values with set
# iterate over unique values
# find indices of unique values, remove them.