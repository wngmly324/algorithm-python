import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

data_set = list(set(data))
data_set.sort()

num = {}
for i in range(len(data_set)):
    num[data_set[i]] = i

for i in data:
    print(num[i], end=' ')