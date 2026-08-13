def multiplication_matrix(A,B):
    return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0]),(A[0][0]*B[0][1]+A[0][1]*B[1][1])],
            [(A[1][0]*B[0][0]+A[1][1]*B[1][0]),(A[1][0]*B[0][1]+A[1][1]*B[1][1])]]

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

n = int(input())
print(fibo_nth(n))