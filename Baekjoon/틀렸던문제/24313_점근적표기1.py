a1, a2 = map(int, input().split())
c = int(input())
n = int(input())

fn = (a1 * n) + a2

if fn <= (c * n) and a1 <= c:
    print(1)
else:
    print(0)
