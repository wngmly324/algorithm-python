square = list([0] * 101 for _ in range(101))

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            square[i][j] = 1

result = 0
for i in range(101):
    for j in range(101):
        if square[i][j] == 1:
            result += 1

print(result)
