n = int(input())
print((n * (n-1) * (n-2)) // 6)
print(3)

# 1부터 n까지의 숫자 중 3가지를 뽑아 중복 없이, 크기 순으로 작성하는 경우의 수가 수행 횟수
# nC3 = n! / (n-3)! * 3!
# 계산하면, (n-2)(n-1)n / 6

# https://dev-mandos.tistory.com/124