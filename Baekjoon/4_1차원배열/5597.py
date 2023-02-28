i = 1
s = []
while i <= 28:
    n = int(input())
    s.append(n)
    i += 1

ss = []

for i in range(1, 31):
    if i not in s:
        ss.append(i)

print(min(ss))
print(max(ss))