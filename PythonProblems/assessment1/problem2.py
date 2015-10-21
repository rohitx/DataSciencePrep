def invert_dictionary(d):
    '''
    INPUT: DICT (STRING => INT)
    OUTPUT: DICT (INT => SET OF STRINGS)

    Given a dictionary d, return a new dictionary with d's values as keys and
    the value for a given key being the set of d's keys which have the same
    value.
    e.g. {'a': 2, 'b': 4, 'c': 2} => {2: {'a', 'c'}, 4: {'b'}}
    '''
    a = {}
    for key, value in d.iteritems():
        if value not in a:
            a[value] = (key)
        else:
            a[value]
    return a

if __name__ == '__main__':
    print invert_dictionary({'a': 2, 'b': 4, 'c': 2})

>>> for key, values in dict1.items():
...     for value in values:
...             dict2.setdefault(value, []).append(key)