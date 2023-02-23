n = int(input())

i = 0
white = []
for i in range(n):
    a = list(map(int, input().split()))
    white.append(a)

n = 19
m = 19
array = [[0] * m for _ in range(n)]

for i in range(len(white)):
    a = white[i][0]
    b = white[i][1]
    array[a-1][b-1] = 1

for i in range(19):
    for j in range(19):
        print(array[i][j], end=" ")
    print()