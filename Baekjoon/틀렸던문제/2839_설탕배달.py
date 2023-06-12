n = int(input())
cnt = 0

while True:
    if n % 5 == 0:
        n -= 5
        cnt += 1
    else:
        n -= 3
        cnt += 1

    if n == 0:
        print(cnt)
        break

    if n < 3:
        print(-1)
        break
