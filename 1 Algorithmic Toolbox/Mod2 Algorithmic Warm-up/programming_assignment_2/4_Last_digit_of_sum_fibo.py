# Last Digit of the Sum of Fibonacci Numbers
# Problem
# Compute the last digit of F0 + F1 + ···+ Fn.
# Input: An integer n.
# Output: The last digit of F0 + F1 +
# ···+ Fn.
# 1 + 1 + 2 + 3 + 5 + 8 = 20
# Input format. An integer n.
# Output format. (F0 + F1 + ···+ Fn) mod 10.
# Constraints. 0 ≤n ≤1014.

def multiply_matrix(A,B):
    return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0])%10,
             (A[0][0]*B[0][1]+A[0][1]*B[1][1])%10],
            [(A[1][0]*B[0][0]+A[1][1]*B[1][0])%10,
             (A[1][0]*B[0][1]+A[1][1]*B[1][1])%10]]

def power_matrix(M,n):
    if n == 0:
        return [[1,0],
                [0,1]]
    if n%2==0:
        return multiply_matrix(power_matrix(M,n//2),power_matrix(M,n//2))
    else:
        return multiply_matrix(power_matrix(M,n-1),M)
def fibo_nums(n):
    M = [[1,1],
         [1,0]]
    if n <=2:
        return 1
    else:
        M_pow_n = power_matrix(M,n)
        return M_pow_n[0][1]
def sum_fibo(n):
    s = 0
    for i in range(n+1):
        s = (s+fibo_nums(i))%10
        print(s)
    return s
n = int(input())
print(sum_fibo(n))