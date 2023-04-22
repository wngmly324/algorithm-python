n = int(input())
data = list(map(int, input().split()))

cnt = 0
for i in data:
    no = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                no += 1
        if no == 0:
            cnt += 1

print(cnt)
