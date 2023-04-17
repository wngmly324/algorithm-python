t = int(input())

data = [25, 10, 5, 1]
for i in range(t):
    c = int(input())

    for j in range(len(data)):
        mo = c // data[j]
        c = c % data[j]
        print(mo, end=' ')
    print()