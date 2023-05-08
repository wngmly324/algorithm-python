import sys

n = int(sys.stdin.readline())
data = []

for _ in range(n):
    xy = list(map(int, sys.stdin.readline().split()))
    data.append(xy)

data = sorted(data, key=lambda x: (x[1], x[0]))

for i in data:
    print(*i)