a, b = input().split()

x = a[-1] + a[1] + a[0]
y = b[-1] + b[1] + b[0]

print(max(int(x), int(y)))