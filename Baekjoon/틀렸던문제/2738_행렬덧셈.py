n, m = map(int, input().split())
a = []
b = []

for i in range(n):
    data = list(map(int, input().split()))
    a.append(data)

for i in range(n):
    data = list(map(int, input().split()))
    b.append(data)

for i in range(n):
    for j in range(m):
        res = a[i][j] + b[i][j]
        print(res, end=' ')
    print()
