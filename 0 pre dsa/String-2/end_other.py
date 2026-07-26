
# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.


# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a,b):
    len_x = min(len(a),len(b))
    a = a.lower()
    b = b.lower()
    for i in range(1, len_x+1):
        if a[-i]!=b[-i]:
            return False
    return True