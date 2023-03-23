n = int(input())

num = []
while n > 0:
    x = int(input())
    num.append(x)

    n -= 1

num.sort()

for i in num:
    print(i)