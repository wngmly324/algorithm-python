a, b, c = map(int, input().split())

if a == b and b == c and c == a:
    res = 10000 + (a * 1000)
elif a != b and b != c and c != a:
    m = max(a, b, c)
    res = m * 100
else:
    if a == b:
        res = 1000 + (a * 100)
    elif b == c:
        res = 1000 + (b * 100)
    else:
        res = 1000 + (c * 100)

print(res)