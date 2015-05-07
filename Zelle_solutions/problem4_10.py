def main():
    string = input("Enter a string: ")
    split_str = string.split()
    count = 0
    sum = 0
    while count < len(split_str):
        sum = sum + len(split_str[count])
        count += 1
    


main()
