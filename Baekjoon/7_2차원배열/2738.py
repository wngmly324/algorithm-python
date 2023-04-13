n, m = map(int, input().split())

m1 = []
m2 = []

for i in range(n):
    x = list(map(int, input().split()))
    m1.append(x)

for i in range(n):
    y = list(map(int, input().split()))
    m2.append(y)

for i in range(n):
    for j in range(m):
        z = m1[i][j] + m2[i][j]
        print(z, end=" ")
    print()