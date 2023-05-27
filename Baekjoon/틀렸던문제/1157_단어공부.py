# import sys
# s = sys.stdin.readline().rstrip()
# s = s.upper()
# data = {}
#
# for i in s:
#     data[i] = s.count(i)
#
# max_val = max(data.values())
# tmp = [k for k, v in data.items() if v == max_val]
#
# if len(tmp) > 1:
#     print('?')
# else:
#     print(*tmp)

import sys
s = sys.stdin.readline().rstrip().upper()
ss = list(set(s))

num = []
for i in ss:
    num.append(s.count(i))

max_num = max(num)
if num.count(max_num) > 1:
    print('?')
else:
    lo = num.index(max_num)
    print(ss[lo])