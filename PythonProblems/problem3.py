"""
Stephan and Sophia forget about security and use simple passwords for everything.
Help Nikola develop a password security check module. The password will be
considered strong enough if its length is greater than or equal to 10 symbols,
it has at least one digit, as well as
containing one uppercase letter and one lowercase letter in it. The password
contains only ASCII latin letters or digits.

Input: A password as a string (Unicode for python 2.7).

Output: Is the password safe or not as a boolean or any data type that can be converted
and processed as a boolean. In the results you will see the converted results.

checkio('A1213pokl') == False
checkio('bAse730onE') == True
checkio('asasasasasasasaas') == False
checkio('QWERTYqwerty') == False
checkio('123456123456') == False
checkio('QwErTy911poqqqq') == True
"""
def checkio(data):
    # check the length
    check_len = len(data) >= 10
    # check if it has words
    wo = [w.isalpha() for w in data]
    check_wo = True in wo
    # check if it has numbers
    no = [n.isdigit() for n in data]
    check_num = True in no
    # check uppercase
    up = [u.isupper() for u in data]
    check_upp = True in up
    # check lowercase
    lo = [l.islower() for l in data]
    check_low = True in lo
    print check_len, check_wo, check_num, check_upp, check_upp
    answer = check_len + check_wo + check_num + check_upp + check_low
    print answer
    if answer == 5:
        return True
    else:
        return False

print checkio('DHJK87DSKJHWW68D')


# Alternate solution
import re
return True if re.search("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$", data) and len(data) >= 10 else False

