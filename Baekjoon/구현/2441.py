n = int(input())

i = 0
while n > 0:
    print(" " * i, end="")
    print("*" * n)

    i += 1
    n -= 1