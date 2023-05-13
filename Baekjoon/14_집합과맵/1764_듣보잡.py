n, m= map(int, input().split())

nlist = set(input() for _ in range(n))
mlist = set(input() for _ in range(m))

result = sorted(list(nlist & mlist))

print(len(result))

for i in result:
    print(i)