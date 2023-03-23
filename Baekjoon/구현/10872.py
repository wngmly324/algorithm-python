n = int(input())

gob = 1
while n > 0:
    gob *= n
    n -= 1

print(gob)