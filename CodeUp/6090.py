a, m, d, n = map(int, input().split())

res = a
cnt = 0

while True:
    cnt += 1

    if cnt == n:
        print(res)
        break

    res = res * m + d