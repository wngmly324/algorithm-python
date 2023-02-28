n = int(input())
d = list(map(int, input().split()))

dd = []
max = max(d)
for i in range(len(d)):
    new = d[i] / max * 100
    dd.append(new)

s = sum(dd)
avg = s / len(dd)

print(avg)