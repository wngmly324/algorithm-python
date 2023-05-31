a, b, v = map(int, input().split())

x = int((v-b) / (a-b))
if (v-b) % (a-b) != 0:
    print(x+1)
else:
    print(x)