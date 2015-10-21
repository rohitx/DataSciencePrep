def count(sequence, item):
    count = 0
    if type(item) == int or type(item) == float:
        for s in sequence:
            if s == item:
                count += 1
        return count
    elif type(item) == str:
        for s in sequence:
            if s.lower() == item.lower():
                count += 1
        return count
    elif type(item) == list:
        for s in sequence:
            for l in item:
                if l == s:
                    count += 1
        return count

if __name__ == '__main__':
    #sequence = [1,2,1,1]
    sequence = ["Hello World", "This World", "I hate this World"]
    print count(sequence, "world")