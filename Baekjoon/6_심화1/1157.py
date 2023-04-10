s = input()

s = s.upper()
ss = set(s)

res = []
for i in ss:
    n = s.count(i)
    res.append(n)

m = max(res)

if res.count(m) > 1:
    print("?")
else:
    ss = list(ss)
    print(ss[res.index(m)])

