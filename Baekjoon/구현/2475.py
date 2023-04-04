data = list(map(int, input().split()))

s = 0
for i in range(len(data)):
    a = data[i] * data[i]
    # b = data[i] ** 2
    # c = pow(data[i], 2)
    s += a

print(s % 10)