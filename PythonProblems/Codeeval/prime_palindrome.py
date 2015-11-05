'''
Write a program which determines the largest prime palindrome less than 1000.

Print to stdout the largest prime palindrome less than 1000

'''
with open('prime_palindrome.txt', 'r') as f:
    data = f.readlines()


pals = 0
for nums in data:
    nums = int(nums)
    if len(str(nums)) < 4 and nums >= pals and str(nums) == str(nums)[::-1]:
        pals = nums
print pals

