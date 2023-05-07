import sys
n = int(sys.stdin.readline())
data = []

for i in range(n):
    xy = list(map(int, sys.stdin.readline().split()))
    data.append(xy)

data.sort()

for i in range(n):
    print(*data[i])