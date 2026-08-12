def GCD(a,b):
    while b!=0:
        b,a = a%b, b
    return a

a,b = map(int,input().split())
print(GCD(a,b))