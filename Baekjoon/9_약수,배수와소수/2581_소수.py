n = int(input())
m = int(input())

data = []
for i in range(n, m+1):
    no = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                no += 1
        if no == 0:
            data.append(i)

if len(data) == 0:
    print(-1)
else:
    print(sum(data))
    print(min(data))