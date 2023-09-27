def solution(num_list):
    answer = 0

    res1 = ''
    res2 = ''
    for i in num_list:
        if i % 2 == 0:
            res1 += str(i)
        else:
            res2 += str(i)

    answer = int(res1) + int(res2)

    return answer