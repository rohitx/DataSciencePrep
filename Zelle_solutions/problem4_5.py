def main():
    string = input("Enter a string: ")
    split_str = string.split()
    count = 0
    acry = ""
    while count < len(split_str):
        acr = split_str[count][0]
        acry += acr
        count += 1
    print acry.upper()
main()
