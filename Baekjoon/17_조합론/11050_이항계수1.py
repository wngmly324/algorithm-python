# n, k = map(int, input().split())
#
# a = n
# aa = 1
# for _ in range(k):
#     aa *= n
#     n -= 1
#
# b = k
# bb = 1
# for i in range(1, k+1):
#     bb *= i
#
# print(aa // bb)

import math
print(math.comb(*map(int, input().split())))