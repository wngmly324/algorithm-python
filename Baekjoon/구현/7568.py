n = int(input())

h = []
for i in range(n):
    x, y = map(int, input().split())
    h.append((x, y))

for i in h:
    rank = 1

    for j in h:
        if(i[0] != j[0]) and (i[1] != j[1]):
            if(i[0] < j[0]) and (i[1] < j[1]):
                rank += 1
    print(rank, end=' ')