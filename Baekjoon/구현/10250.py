t = int(input())

while t > 0:
    h, w, n = map(int, input().split())

    for i in range(1, w+1):
        for j in range(1, h+1):
            if i < 10:
                res = str(j) + "0" + str(i)
                n -= 1
            else:
                res = str(j) + str(i)
                n -= 1

            if n == 0:
                print(res)
                break
    t -= 1