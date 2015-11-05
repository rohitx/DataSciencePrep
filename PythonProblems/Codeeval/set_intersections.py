'''
File containing two lists of ascending order sorted integers,
comma delimited, one per line. E.g. 


INPUT
1,2,3,4;4,5,6
20,21,22;45,46,47
7,8,9;8,9,10,11,12

OUTPUT
4

8,9
'''

with open('set_intersections.txt', 'r') as f:
    data = f.readlines()

for d in data:
    values = d.strip().split(";")
    set1 = set([int(i) for i in values[0].split(",")])
    set2 = set([int(i) for i in values[1].split(",")])
    print ",".join(map(str, list(set1.intersection(set2))))
