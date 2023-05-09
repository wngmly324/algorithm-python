n = int(input())
datas = []

for _ in range(n):
    mem = list(input().split())
    datas.append(mem)

datas = sorted(datas, key=lambda x: int(x[0]))

for i in range(len(datas)):
    print(datas[i][0], datas[i][1])