# import math
#
# a, b = map(int, input().split())
# c, d = map(int, input().split())
#
# r1 = (a * d) + (c * b)
# r2 = b * d
#
# gcd = math.gcd(r1, r2)
# r1 //= gcd
# r2 //= gcd
#
# print(r1, r2)

"""분모와 분자를 각각 최대공약수로 나눈 값이 곧 기약분수"""

a, b = map(int, input().split())
c, d = map(int, input().split())

r1 = (a * d) + (c * b)
r2 = b * d

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

gcd = gcd(r1, r2)

r1 = int(r1 / gcd)
r2 = int(r2 / gcd)

print(r1, r2)