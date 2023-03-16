n, k = map(int, input().split())

cList = []
while n > 0:
    c = int(input())
    cList.append(c)

    n -= 1
cList.reverse()

cnt = 0
while k != 0:
    if n == 1:
        cnt += k // cnt[0]
        k = 0
    for i in range(len(cList)):
        if k // cList[i] != 0:
            d = cList[i]
            break

    cnt += k // d
    k = k % d

print(cnt)