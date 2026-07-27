
# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

def sum67(nums):
    sum1 = 0
    sum2 = 0
    for n in nums:
        if sum2 == 0:
            if n != 6:
                sum1 += n
            else:
                sum2 += n
        else:
            if n == 7:
                sum2 = 0
            else:
                sum2 += n
    return sum1+sum2