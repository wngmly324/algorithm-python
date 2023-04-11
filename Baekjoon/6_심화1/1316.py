n = int(input())

cnt = n
while n:
    a = input()
    for j in range(len(a)-1):
        if a[j] == a[j+1]:
            pass
        elif a[j] in a[j+1:]:
            cnt -= 1
            break
    n -= 1

print(cnt)