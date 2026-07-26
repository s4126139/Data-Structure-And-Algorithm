
# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.


# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(str):
    if 'xyz' not in str:
        return False
    else:
        count = 0
        if str[0:3] == 'xyz':
            count += 1
        for i in range(1,len(str)-2):
            if str[i:i+3] == 'xyz' and str[i-1] != '.':
                count += 1
        return count != 0