n, k = map(int, input().split())

data= []
for i in range(1, n+1):
    re = n % i
    if re == 0:
        data.append(i)

if len(data) < k:
    print(0)
else:
    print(data[k-1])