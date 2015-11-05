'''
INPUT:
1,1,1,2,2,3,3,4,4
2,3,4,5,5

OUTPUT:
1,2,3,4
2,3,4,5
'''


with open('unique_elements.txt', "r") as f:
    data = f.readlines()

for d in data:
    the_list = d.split(",")
    unique = list(set([int(v) for v in the_list]))
    print ','.join(map(str, unique))
