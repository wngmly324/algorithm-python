n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

data = sorted(data, key=lambda x: (x[1], x[0]))

for i in data:
    print(*i)