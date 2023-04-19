a, b, v = map(int, input().split())

day = (v-a) // (a-b)
gal = (v-a) % (a-b)

if gal == 0:
    print(day+1)
elif gal > 0:
    print(day+2)
