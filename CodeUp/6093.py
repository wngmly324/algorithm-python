n = int(input())
sList = list(map(int, input().split()))

sList.reverse()

for i in sList:
    print(i, end=" ")