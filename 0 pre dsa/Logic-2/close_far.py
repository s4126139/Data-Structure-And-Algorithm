
# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.


# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True

def close_far(a, b, c):
    a_close_b = (abs(a-b)<=1)
    a_close_c = (abs(a-c)<=1)
    a_far_b = (abs(a-b)>=2)
    a_far_c = (abs(a-c)>=2)
    b_far_c = (abs(b-c)>=2)
    if (a_close_b or a_close_c) and (a_far_b or a_far_c) and b_far_c:
        return True
    else:
        return False
    