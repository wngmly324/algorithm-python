s = input()

data = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in data:
    if i in s:
        s = s.replace(i, "*")

print(len(s))