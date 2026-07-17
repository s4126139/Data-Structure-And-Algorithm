# Given a string, return a new string where the first and last chars have been exchanged.


# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'
def front_back(str):
    if len(str) <= 1:
        return str
    else:
        n = len(str)-1
        return str[n]+str[1:n]+str[0]