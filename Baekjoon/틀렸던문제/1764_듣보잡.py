import sys

n, m = map(int, sys.stdin.readline().split())
data = {}
cnt = 0

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    data[s] = 1

for _ in range(m):
    r = sys.stdin.readline().rstrip()

    if r in data:
        data[r] += 1
        cnt += 1

data = dict(sorted(data.items(), key=lambda x: x[0]))

print(cnt)

for key, value in data.items():
    if value >= 2:
        print(key)