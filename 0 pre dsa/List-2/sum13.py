
# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
    s = 0
    skip = False
    for i in nums:
        if i == 13:
            skip = True
            continue
        if skip:
            skip = False
            continue
        s += i
    return s