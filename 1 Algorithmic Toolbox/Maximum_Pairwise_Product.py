# import random

# def max_pairwise_product_naive(numbers):
#     result = 0
#     n = len(numbers)

#     for i in range(n):
#         for j in range(i + 1, n):
#             result = max(result, numbers[i] * numbers[j])

#     return result


def max_pairwise_product_fast(numbers):
    if numbers[0] >= numbers[1]:
        max1 = numbers[0]
        max2 = numbers[1]
    else:
        max1 = numbers[1]
        max2 = numbers[0]

    for x in numbers[2:]:
        if x >= max1:
            max2 = max1
            max1 = x
        elif x > max2:
            max2 = x

    return max1 * max2


# while True:
#     n = random.randint(2, 10)
#     numbers = [random.randint(0, 20) for _ in range(n)]

#     naive = max_pairwise_product_naive(numbers)
#     fast = max_pairwise_product_fast(numbers)

#     if naive != fast:
#         print("Wrong answer!")
#         print("numbers:", numbers)
#         print("naive:", naive)
#         print("fast:", fast)
#         break
#     else:
#         print("OK")