# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.


# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
    max_nums = nums[0]
    min_nums = nums[0]
    s = nums[0]
    for i in nums[1:]:
        if i >= max_nums: max_nums = i
        if i <= min_nums: min_nums = i
        s += i
    return (s-max_nums-min_nums)/(len(nums)-2)