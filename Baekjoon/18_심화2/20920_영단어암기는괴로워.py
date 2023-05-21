import sys

n, m = map(int, sys.stdin.readline().split())
dic = {}

for _ in range(n):
    s = sys.stdin.readline().rstrip()

    if len(s) < m:
        continue
    else:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1

sort_dic = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in sort_dic:
    print(i[0])