x, y, w, h = map(int, input().split())

data = []

data.append(x)
data.append(y)

r1 = w - x
r2 = h - y
data.append(r1)
data.append(r2)

print(min(data))