n = int(input())

sum = 0
cnt = 0
i = 1

while sum < n:
    sum += i
    cnt += 1
    i += 1

print(cnt)
