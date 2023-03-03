s = input()

a = []
for i in range(97, 123):
    a.append(chr(i))

for i in range(len(a)):
    if a[i] in s:
        n = a.index(a[i])
        a[n] = s.index(a[i])
    else:
        a[i] = -1

for i in a:
    print(i, end=" ")