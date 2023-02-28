i = 0
nList = []
while i < 10:
    n = int(input())
    r = n % 42
    nList.append(r)

    i += 1

nSet = set(nList)

if not nSet:
    print("1")
else:
    print(len(nSet))