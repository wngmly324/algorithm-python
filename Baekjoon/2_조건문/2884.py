h, m = map(int, input().split())

if m >= 45:
    print(h, m-45)
else:
    num = 45 - m

    if h == 0:
        print(23, 60-num)
    else:
        print(h-1, 60-num)