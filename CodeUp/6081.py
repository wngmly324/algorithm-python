n = int(input(), 16)

for i in range(1, 16):
    print("%X" % n, end="")
    print("*%X" % i, end="")
    print("=%X" % (n*i))