w, h = map(int, input().split())
pan = [[0] * h for _ in range(w)]

n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            pan[x-1][y-1+j] = 1
    else:
        for j in range(l):
            pan[x-1+j][y-1] = 1

for i in range(w):
    for j in range(h):
        print(pan[i][j], end=" ")
    print()