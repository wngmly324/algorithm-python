data = sorted(list(map(int, input().split())))

if data[0] + data[1] > data[2]:
    print(sum(data))
else:
    print((data[0] + data[1]) * 2 - 1)