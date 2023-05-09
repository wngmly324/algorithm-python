import sys

n = int(input())
datas = list(map(int, sys.stdin.readline().split()))

datas2 = sorted(list(set(datas)))

numdict = {}
for i in range(len(datas2)):
    numdict[datas2[i]] = i

for i in datas:
    print(numdict[i], end=' ')