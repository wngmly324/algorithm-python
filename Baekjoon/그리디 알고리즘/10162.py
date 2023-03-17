t = int(input())

a = 5 * 60
b = 1 * 60
c = 10

abc = [a, b, c]

for i in range(len(abc)):
    if t % c != 0:
        print("-1")
        break
    else:
        cnt = 0
        cnt += t // abc[i]
        t = t % abc[i]
        print(cnt, end=" ")