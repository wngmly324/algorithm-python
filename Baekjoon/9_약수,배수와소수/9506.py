while True:
    n = int(input())

    data = []

    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            data.append(i)

    s = sum(data)
    if s != n:
        print("%d is NOT perfect." % n)
    else:
        print(n, "= ", end="")

        strr = ""
        for i in data:
            strr += str(i) + " "

        strr = strr.replace(" ", " + ")
        print(strr[:-2])