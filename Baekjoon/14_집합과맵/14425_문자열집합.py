n, m = map(int, input().split())

nlist = set([input() for _ in range(n)])
cnt = 0

for i in range(m):
    s = input()

    if s in nlist:
        cnt += 1

print(cnt)