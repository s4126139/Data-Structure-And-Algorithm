#O(n^2)-> out of memory
def huge_fibonnaci_number(n,m):
    F=[0]*(n+1)
    F[0],F[1] = 0,1
    for i in range(2,n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n] % m

n, m = map(int, input().split())
print(huge_fibonnaci_number(n,m))