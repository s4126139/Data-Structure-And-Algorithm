def multiplication_matrix(A,B):
    return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0])%10,(A[0][0]*B[0][1]+A[0][1]*B[1][1])%10],
            [(A[1][0]*B[0][0]+A[1][1]*B[1][0])%10,(A[1][0]*B[0][1]+A[1][1]*B[1][1])%10]]

def fibo_nth(n):
    result = [[1,0],
              [0,1]]
    base = [[1,1],
            [1,0]]
    while n:
        if n & 1:
            result = multiplication_matrix(result,base)
        base = multiplication_matrix(base,base)
        n >>=1
    return result[0][1]

def last_digit_of_partial_sum(m,n):
    if m == n:
        return fibo_nth(n)
    return (fibo_nth(n+2)-fibo_nth(m+1))%10

m,n = map(int,input().split())
print(last_digit_of_partial_sum(m,n))