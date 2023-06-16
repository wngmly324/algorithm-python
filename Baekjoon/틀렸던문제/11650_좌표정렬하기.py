import sys

n = int(input())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

data = sorted(data, key=lambda x: (x[0], x[1]))

for i in data:
    print(*i)