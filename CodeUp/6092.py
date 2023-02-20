n = int(input())
sList = list(map(int, input().split()))

res = []

for i in range(1, 24):
    num = sList.count(i)
    res.append(num)

for i in res:
    print(i, end=" ")