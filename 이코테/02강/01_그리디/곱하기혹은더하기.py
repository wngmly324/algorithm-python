s = input()

res = 0
for i in range(len(s)):
    if int(s[i]) == 0 or int(s[i]) == 1 or res == 0:
        res += int(s[i])
    else:
        res *= int(s[i])

print(res)

########################################################

data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹인 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)