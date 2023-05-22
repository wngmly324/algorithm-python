k = int(input())
data = []

for _ in range(k):
    s = int(input())

    if s == 0:
        data.pop()
    else:
        data.append(s)

print(sum(data))