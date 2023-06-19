a, b = map(int, input().split())
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

res = (setA - setB)
res2 = (setB - setA)
print(len(res) + len(res2))