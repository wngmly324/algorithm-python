xx = []
yy = []
for i in range(3):
    x, y = map(int, input().split())
    xx.append(x)
    yy.append(y)

for i in range(3):
    if xx.count(xx[i]) == 1:
        print(xx[i], end=" ")

for i in range(3):
    if yy.count(yy[i]) == 1:
        print(yy[i])
