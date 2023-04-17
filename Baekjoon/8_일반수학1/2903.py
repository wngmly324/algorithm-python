n = int(input())

i = 2
if n == 0:
    print(i * i)
else:
    d = 1
    for _ in range(n):
        i += d
        d *= 2

print(i * i)
