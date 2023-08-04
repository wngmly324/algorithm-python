n, b = input().split()

print(int(n, int(b)))

#######################

a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = input().split()

n = n[::-1]
ans = 0
for i in range(len(n)):
    ans += a.find(n[i]) * int(b) ** i

print(ans)
