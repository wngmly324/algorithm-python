def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
def lcm(x, y):
    result = (x * y) // gcd(x, y)
    return result

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    print(lcm(x, y))