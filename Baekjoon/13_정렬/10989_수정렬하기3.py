import sys

n = int(sys.stdin.readline())
data = [0] * 10001

for i in range(n):
    data[int(sys.stdin.readline())] += 1

for i in range(10001):
    if data != 0:
        for j in range(data[i]):
            print(i)