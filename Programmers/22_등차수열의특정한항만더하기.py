def solution(a, d, included):
    answer = 0

    for i in range(len(included)):
        res = a + d * i

        if included[i] == True:
            answer += res

    return answer