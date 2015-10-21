def median(a_list):
    sorted_list = sorted(a_list)
    list_len = len(sorted_list)
    mid_point = list_len / 2
    if list_len%2 == 0:
        median_val = (sorted_list[mid_point] + sorted_list[mid_point-1])/2.
        return median_val
    else:
        median_val = sorted_list[mid_point]
        return median_val

if __name__ == '__main__':
    #a_list = [7,3,1,4,10,12]
    a_list = [7,3,1,4]
    print median(a_list)