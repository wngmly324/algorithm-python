import sys

k = int(sys.stdin.readline())

result = []
while k > 0:
    n = int(sys.stdin.readline())

    if n == 0:
        result.pop()
    else:
        result.append(n)

    k -= 1

print(sum(result))