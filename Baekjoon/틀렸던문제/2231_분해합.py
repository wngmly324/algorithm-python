n = int(input())

for i in range(1, n + 1):
    num = sum((map(int, str(i))))  # i의 각 자릿수를 더함
    num_sum = i + num  # 분해합 = 생성자 + 각 자릿수의 합

    # i가 작은 수부터 차례로 들어가므로 처음으로 분해합과 입력값이 같을 때가 가장 작은 생성자르 가짐
    if num_sum == n:
        print(i)
        break
    if i == n:  # 생성자 i와 입렵값이 같다는 것은 생성자가 없다는 뜻
        print(0)

# a, b, c = map(int, str(198))
# print(a, b, c)
# 1 9 8
