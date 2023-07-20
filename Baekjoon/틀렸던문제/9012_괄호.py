import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline()
    data = []

    for i in s:
        if i == '(':
            data.append(i)
        elif i == ')':
            if data:
                data.pop()
            else:
                print("NO")
                break
        else:
            if not data:
                print("YES")
            else:
                print("NO")