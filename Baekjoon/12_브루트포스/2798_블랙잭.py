import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

def black_jack(m, card_list):
    arr = []

    for cards in combinations(card_list, 3):
        if sum(cards) <= m:
            arr.append(sum(cards))

    return max(arr)

print(black_jack(m, num_list))