n = int(input())
datas = []
lendata = []

for _ in range(n):
    a = input()
    la = len(a)
    li = [a, la]
    datas.append(li)

datas.append([0, 20001])
datas = sorted(datas, key=lambda x: (x[1], x[0]))

for i in range(len(datas)-1):
    if datas[i] == datas[i+1]:
        continue
    else:
        print(datas[i][0])