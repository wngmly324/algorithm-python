n = int(input())

dic = {}
cnt = 0

for _ in range(n):
    s = input()

    if s == "ENTER":
        for key, value in dic.items():
            if value == 1:
                cnt += 1
        dic = {}
    else:
        if s not in dic:
            dic[s] = 1

for key, value in dic.items():
    if value == 1:
        cnt += 1

print(cnt)