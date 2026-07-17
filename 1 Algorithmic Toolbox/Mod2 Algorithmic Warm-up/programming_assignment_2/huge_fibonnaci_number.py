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

def multiply_matrix(A,B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def power_matrix(M,n):
    if n%2 == 0:
        return multiply_matrix(power_matrix(M,n/2),power_matrix(M,n/2))
    else:
        return multiply_matrix()

def huge_fibonnaci_number(n,m):
    if n <= 1:
        return n%m
    else:
        M = [[1,1],
             [1,0]]
        power_matrix(M,n)

n, m = map(int, input().split())
print(huge_fibonnaci_number(n,m))