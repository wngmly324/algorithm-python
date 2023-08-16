data = list(map(int, input().split()))
data.sort()

if data[0] + data[1] > data[2]:
    print(sum(data))
else:
    print((data[0] + data[1]) * 2 - 1)

# 삼각형의 필수 조건에 의해 작은 두 수의 합이 가장 큰 수보다 크다면
# 전체의 합을 출력하고, 작거나 같다면 작은 두 수의 합의 두 배에서 1을 뺀 값을 출력한다.
