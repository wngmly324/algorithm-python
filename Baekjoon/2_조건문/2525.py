h, m = map(int, input().split())
t = int(input())

a = t // 60
b = t % 60

if t >= 60:
    if m + b >= 60:
        if h+a+1 >= 24:
            print(h+a+1-24, m+b-60)
        else:
            print(h+a+1, m+b-60)
    else:
        if h+a >= 24:
            print(h+a-24, m+b)
        else:
            print(h+a, m+b)
else:
    if m + b >= 60:
        if h+1 >= 24:
            print(h+1-24, m+t-60)
        else:
            print(h+1, m+t-60)
    else:
        print(h, m+t)