s = input()
s = s.upper()
sl = list(set(s))

cnt = []
for i in sl:
    c = s.count(i)
    cnt.append(c)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(sl[cnt.index(max(cnt))])