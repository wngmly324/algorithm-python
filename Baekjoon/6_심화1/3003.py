data = [1, 1, 2, 2, 2, 8]

my = list(map(int, input().split()))

for i in range(len(data)):
    if data[i] == my[i]:
        print("0", end=' ')
    else:
        print(data[i] - my[i], end=' ')