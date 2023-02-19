a, d, n = map(int, input().split())

cnt = 1
sum = a
while True:
    sum += d
    cnt += 1

    if cnt == n:
        print(sum)
        break