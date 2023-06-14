n = int(input())
data = {}

for i in range(n):
    s = input()
    sl = len(s)

    if s in data:
        continue
    else:
        data[s] = sl

data = list(sorted(data.items(), key=lambda x: (x[1], x[0])))

for i in range(len(data)):
    print(data[i][0])