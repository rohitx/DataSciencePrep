def sum_of_digits(num):
    number_str = str(num)
    value = sum([int(d) for d in number_str])
    return value

if __name__ == '__main__':
    print sum_of_digits(496)