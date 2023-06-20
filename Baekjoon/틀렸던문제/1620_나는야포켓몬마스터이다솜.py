import sys
n, m = map(int, sys.stdin.readline().split())
data = {}

for i in range(1, n+1):
    p = sys.stdin.readline().rstrip()
    data[p] = i
    data[i] = p

for _ in range(m):
    s = sys.stdin.readline().rstrip()

    if s.isdigit():
        print(data[int(s)])
    else:
        print(data[s])