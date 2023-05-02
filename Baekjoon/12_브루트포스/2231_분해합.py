n = int(input())

for i in range(1, n+1):
    if i == n:
        print(0)
    if i + sum(map(int, str(i))) == n:
        print(i)
        break

# a, b, c = map(int, str(198))
# print(a, b, c)
# 1 9 8