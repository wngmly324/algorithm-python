n, m = map(int, input().split())

list = []

for x in range(1, n+1):
    list.append(x)

for y in range(m):
    i, j = map(int, input().split())
    a = list[i-1]
    b = list[j-1]
    list[j-1] = a
    list[i-1] = b

for z in list:
    print(z, end=" ")