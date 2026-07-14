def last_digit_of_fibo_array(n):
    F=[0]*(n+1)
    F[0],F[1]=0,1
    for i in range(2,n+1):
        F[i]=F[i-1]+F[i-2]
    return F[n]%10

n = int(input())
print(last_digit_of_fibo_array(n))

    