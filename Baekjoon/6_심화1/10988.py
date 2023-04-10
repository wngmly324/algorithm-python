s = input()

n = len(s) // 2
j = -1
res = []
for i in range(n):
    if s[i] != s[j]:
        res.append(0)
    else:
        res.append(1)
    j -= 1

if 0 in res:
    print(0)
else:
    print(1)