import sys

n, m = map(int, sys.stdin.readline().split())
data = dict()

for _ in range(n):
    s = sys.stdin.readline().rstrip()

    if s in data:
        data[s] += 1
    elif len(s) >= m:
        data[s] = 1

data = sorted(data.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in range(len(data)):
    print(data[i][0])