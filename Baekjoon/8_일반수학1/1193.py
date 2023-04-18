x = int(input())

cnt = 0
i = 0
while cnt < x:
    i += 1
    cnt += i

cnt -= i
tmp = x - cnt
if i % 2 == 0:
    m = 1 + (tmp - 1)
    n = i - (tmp - 1)
else:
    m = i - (tmp - 1)
    n = 1 + (tmp - 1)

print(f'{m}/{n}')