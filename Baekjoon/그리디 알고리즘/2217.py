s = int(input())

sum = 0
cnt = 0

i = 0
while True:
    i += 1
    sum += i

    if sum > s:
        break

    cnt += 1

print(cnt)