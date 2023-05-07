s = list(input())
data = []

for i in s:
    data.append(int(i))

data.sort(reverse=True)
for i in data:
    print(i, end="")