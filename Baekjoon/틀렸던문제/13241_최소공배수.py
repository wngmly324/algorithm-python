a, b = map(int, input().split())

def gcd(a, b):
    while a % b != 0:
        mod = a % b
        a = b
        b = mod
    return b

print(a*b // gcd(a, b))
