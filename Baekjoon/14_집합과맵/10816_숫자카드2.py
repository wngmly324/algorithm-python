import sys

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
mlist = list(map(int, sys.stdin.readline().split()))

cnt = {}
for i in nlist:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in mlist:
    result = cnt.get(i)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")