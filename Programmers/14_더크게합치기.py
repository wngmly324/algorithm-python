def solution(a, b):
    answer = 0

    res1 = int(str(a) + str(b))
    res2 = int(str(b) + str(a))

    if res1 > res2:
        answer = res1
    else:
        answer = res2

    return answer