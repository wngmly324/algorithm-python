def gcd(x, y):
    if x < y:
        tmp = x
        x = y
        y = tmp
    while y != 0:
        n = x % y
        x = y
        y = n
    return x

def lcm(x, y):
    result = (x * y) // gcd(x, y)
    return result

x, y = map(int, input().split())

print(lcm(x, y))