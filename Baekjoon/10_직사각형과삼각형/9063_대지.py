n = int(input())

x = []
y = []
for i in range(n):
    xx, yy = map(int, input().split())
    x.append(xx)
    y.append(yy)

if len(x) < 2:
    print(0)
else:
    mx = max(x)
    my = max(y)
    mix = min(x)
    miy = min(y)
    print((mx-mix) * (my - miy))