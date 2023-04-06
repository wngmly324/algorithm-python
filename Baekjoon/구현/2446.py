n = int(input())
nn = n

i = 0
while n > 1:
    print(" " * i, end="")
    print("*" * (n * 2 - 1))
    i += 1
    n -= 1

j = 1
while nn > 0:
    print(" " * (nn-1), end="")
    print("*" * j)
    nn -= 1
    j += 2