def solution(l, r):
    answer = []

    for i in range(l, r + 1):
        s = str(i)

        tmp = []
        for j in range(len(s)):
            if s[j] == '5' or s[j] == '0':
                tmp.append(1)
            else:
                tmp.append(0)

        if 0 in tmp:
            pass
        else:
            answer.append(i)

    return answer if len(answer) > 0 else [-1]