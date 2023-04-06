t = int(input())

change = [25, 10, 5, 1]

while t > 0:
    ch = int(input())

    for i in change:
        m = ch // i
        ch = ch % i
        print(m, end=" ")
    print()

    t -= 1