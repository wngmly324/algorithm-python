n = int(input())

i = 0
while i < n:
    a, b = map(int, input().split())
    print("Case #%d: %d" % (i+1, a+b))

    i += 1