def solution(num_list):
    answer = 0

    res1 = 1
    res2 = sum(num_list) ** 2
    for i in num_list:
        res1 *= i

    print(res1, res2)

    if res1 < res2:
        answer = 1
    else:
        answer = 0

    return answer