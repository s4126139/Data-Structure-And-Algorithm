def GCD(a,b):
    while b!=0:
        b,a = a%b, b
    return a
