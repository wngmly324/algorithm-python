n = int(input())
cnt = 0

if n % 5 == 0:
    cnt = n // 5
    print(cnt)
else:
    while n > 0:
        n -= 3
        cnt += 1

        if n % 5 == 0:
            r = n // 5
            cnt += r
            print(cnt)
            break
        elif n < 3:
            print(-1)
            break