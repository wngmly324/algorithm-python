from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

c_c = list(set(combinations(cards, 3)))

res = []
for i in range(len(c_c)):
    s_s = sum(c_c[i])
    res.append(s_s)

res.sort()

if max(res) <= m:
    print(max(res))
else:
    for i in range(len(res)):
        if res[i] > m:
            print(res[i-1])
            break