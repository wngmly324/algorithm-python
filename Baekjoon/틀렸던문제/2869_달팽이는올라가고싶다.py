a, b, v = map(int, input().split())

res = int((v - b) / (a - b))
if (v - b) % (a - b) != 0:
    print(res + 1)
else:
    print(res)
