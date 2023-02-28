p = int(input())
c = int(input())

sum = 0
for i in range(c):
    a, b = map(int, input().split())
    gob = a * b
    sum += gob

if p == sum:
    print("Yes")
else:
    print("No")