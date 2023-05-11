import sys

n = int(sys.stdin.readline())
card = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

for i in range(len(data)):
    if data[i] in card:
        print(1, end=' ')
    else:
        print(0, end=' ')
