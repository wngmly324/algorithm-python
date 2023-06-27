n = int(input())
data = {}

for _ in range(n):
    a, b = map(str, input().split())

    if b == "enter":
        data[a] = b
    else:
        del data[a]

data = sorted(data.keys(), reverse=True)

for i in data:
    print(i)