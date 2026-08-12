def multiply_matrix(A,B):
    return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0])%10,(A[0][0]*B[0][1]+A[0][1]*B[1][1])%10],
            [(A[1][0]*B[0][0]+A[1][1]*B[1][0])%10,(A[1][0]*B[0][1]+A[1][1]*B[1][1])%10]]


def fibo_nth_and_nth_plus1(n):
    result = [[1,0],
              [0,1]]
    M = [[1,1],
         [1,0]]
    while n:
        if n & 1:
            result = multiply_matrix(result, M)
        M = multiply_matrix(M, M)
        n >>= 1

    return result[0][1], result[0][0]

def last_digit_of_sum_squares_fibo(n):
    if n <= 1:
        return n

    nth, nth_plus1 = fibo_nth_and_nth_plus1(n)
    return (nth * nth_plus1) % 10

print(last_digit_of_sum_squares_fibo(int(input())))