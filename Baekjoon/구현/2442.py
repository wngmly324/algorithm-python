n = int(input())

j = 1
while n > 0:
    print((n-1) * " ", end="")
    print(j * "*")
    j += 2
    n -= 1