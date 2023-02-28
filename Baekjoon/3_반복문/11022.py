n = int(input())

i = 0
while i < n:
    a, b = map(int, input().split())
    print("Case #%d:" % (i+1), end=" ")
    print("%d + %d = %d" % (a, b, (a+b)))

    i += 1