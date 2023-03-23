n = int(input())

f0 = 0
f1 = 1

if n == 0:
    print(f0)
elif n == 1:
    print(f1)
else:
    for i in range(n-1):
        f = f0 + f1
        f0 = f1
        f1 = f
    print(f)

##########################
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))