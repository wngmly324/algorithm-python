data = list(map(int, input().split()))

c = [1, 1, 2, 2, 2, 8]

for i in range(len(data)):
    if data[i] == c[i]:
        print(0, end=' ')
    else:
        print(c[i] - data[i], end=' ')
