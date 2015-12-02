with open('sum_of_integers.txt', "r") as f:
    data = f.readlines()

value = sum([int(w) for w in data])
print value