data = []
for i in range(5):
    n = int(input())
    data.append(n)

data.sort()

print("%d" % (sum(data) / 5))
print(data[2])