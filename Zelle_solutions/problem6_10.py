def acronmy(phrase):
    string = phrase.strip().split(" ")
    count = 0
    sum = ""
    while count < len(string):
        sum = sum + string[count][0]
        count += 1
    return sum.upper()

print acronmy("rohit shrikant deshpande")
