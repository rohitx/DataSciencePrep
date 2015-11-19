'''
Using the Python language, have the function SecondGreatLow(arr) take the array of numbers stored in arr and return the second lowest and second greatest numbers, respectively, separated by a space. For example: if arr contains [7, 7, 12, 98, 106] the output should be 12 98. The array will not be empty and will contain at least 2 numbers. It can get tricky if there's just two numbers!

'''
def SecondGreatLow(arr):
    max_val = max([n for n in arr if n!= max(arr)])
    min_val = min([n for n in arr if n!=min(arr)])
    result = str(min_val) + " " + str(max_val)
    return  result






# keep this function call here
# to see how to enter arguments in Python scroll down
#print SecondGreatLow([7, 7, 12, 98, 106])
#print SecondGreatLow([1,42,42,180])
print SecondGreatLow([4,90])