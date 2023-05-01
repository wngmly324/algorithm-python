a1, a2 = map(int, input().split())
c = int(input())
n0 = int(input())

f = (a1 * n0) + a2
g = n0

if f <= (c * g) and c >= a1:
    print(1)
else:
    print(0)