n, m = map(int, input().split())

l = []
for i in range(1, n+1):
    l.append(i)

for x in range(m):
    i, j = map(int, input().split())
    ll = l[i-1:j]
    ll.reverse()

    for y in ll:
        l[i-1] = y
        i += 1

for i in l:
    print(i, end=" ")