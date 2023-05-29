n, m = map(int, input().split())
a = [[0] * m for _ in range(n)]

for i in range(n):
    inp = list(map(int, input().split()))
    for j in range(m):
        a[i][j] = inp[j]

for i in range(n):
    inp2 = list(map(int, input().split()))
    for j in range(m):
        a[i][j] += inp2[j]

for i in a:
    print(*i)