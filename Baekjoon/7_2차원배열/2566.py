n = 9
m = 9
data = []
maxData = []

for i in range(n):
    x = list(map(int, input().split()))
    data.append(x)
    y = max(x)
    maxData.append(y)

maxNum = max(maxData)
print(maxNum)

for i in range(n):
    for j in range(m):
        if data[i][j] == maxNum:
            print(i+1, j+1)
            break