def GCD(a,b):
    while b != 0:
        b, a = a%b, b
    return a

def lcm(a,b):
    gcd_ab = GCD(a,b)
    return int(a/gcd_ab)*int(b/gcd_ab)*gcd_ab

a,b = map(int,input().split())
print(lcm(a,b))