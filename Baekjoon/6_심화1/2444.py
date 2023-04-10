n = int(input())

i = 1
t = n-1
for _ in range(n-1):
    print(" " * t, end="")
    print("*" * i)

    t -= 1
    i += 2

nn = (2 * n) - 1
for i in range((nn-n)+1):
    print(" " * i, end="")
    print("*" * nn)

    nn -= 2