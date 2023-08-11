n = int(input())
num_list = list(map(int, input().split()))

cnt = 0

for i in num_list:
    no = 0
    if i > 1:
        for j in range(2, i+1):
            if i % j == 0:
                no += 1

        if no == 1:
            cnt += 1

print(cnt)
