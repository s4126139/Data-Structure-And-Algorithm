# #O(n) time complexity and O(n) space complexity
# # Time complexity: O(n^2) when counting big-integer addition cost
# #F[i] has about Theta(i) digits, so addition at step i costs Theta(i)
# def huge_fibonnaci_number(n,m):
#     F=[0]*(n+1)
#     F[0],F[1] = 0,1
#     for i in range(2,n+1):
#         F[i] = F[i-1] + F[i-2]
#     return F[n] % m

# #O(n) time complexity and O(1) space complexity
# #Have to wait if n is so big
# def huge_fibonnaci_number(n,m):
#     if n <= 1:
#         return n%m
#     else:
#         a, b = 0, 1
#         for i in range(2,n+1):
#             if i % 2 == 0:
#                 a = (a+b)%m
#             else:
#                 b = (a+b)%m
#     if n % 2 == 0:
#         return a 
#     else: return b



n, m = map(int, input().split())
print(huge_fibonnaci_number(n,m))