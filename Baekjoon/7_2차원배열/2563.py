data = [[0] * 100 for _ in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            data[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if data[i][j] == 1:
            cnt += 1

print(cnt)