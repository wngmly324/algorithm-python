n = int(input())
p = list(map(int, input().split()))

p.sort()

ss = 0
rr = []
for i in p:
    ss += i
    rr.append(ss)

print(sum(rr))