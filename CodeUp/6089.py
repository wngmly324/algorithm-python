a, r, n = map(int, input().split())

cnt = 1
gob = a

while True:
    gob *= r
    cnt += 1

    if cnt == n:
        print(gob)
        break