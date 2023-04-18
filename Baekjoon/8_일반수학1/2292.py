n = int(input())

i = 1
res = 0
cnt = 1
if n == 1:
    print(cnt)
else:

    while True:
        cnt += 1
        res += 6 * i
        i += 1

        if (res+1) >= n:
            print(cnt)
            break