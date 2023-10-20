def solution(intStrs, k, s, l):
    answer = []

    for i in range(len(intStrs)):
        st = intStrs[i]
        tmp = st[s:s + l]

        if int(tmp) > k:
            answer.append(int(tmp))

    return answer