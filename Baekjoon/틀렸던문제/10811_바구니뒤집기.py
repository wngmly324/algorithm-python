n, m = map(int, input().split())
data = [i for i in range(1, n+1)]

for _ in range(m):
    a, b = map(int, input().split())

    s = data[a-1:b]
    s.reverse()

    data[a-1:b] = s

print(*data)