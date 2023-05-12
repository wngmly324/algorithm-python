import sys

n, m = map(int, sys.stdin.readline().split())

data = {}
for i in range(1, n+1):
    a = sys.stdin.readline().rstrip()
    data[i] = a
    data[a] = i

for i in range(m):
    p = sys.stdin.readline().rstrip()

    if p.isdigit():
        print(data[int(p)])
    else:
        print(data[p])