b, n = map(int, input().split())

list = []
for _ in range(b):
    data = []
    list.append(data)

for x in range(n):
    i, j, k = map(int, input().split())

    if i == j:
        list[i-1].append(k)
    else:
        for y in range(i, j+1):
            list[y-1].append(k)

for i in range(len(list)):
    # if len(list[i]) == 0:
    if not list[i]:
        print(0, end=" ")
    else:
        print(list[i][-1], end=" ")