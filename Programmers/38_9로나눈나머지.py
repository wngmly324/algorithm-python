def solution(number):
    n_sum = 0
    for i in str(number):
        n_sum += int(i)

    answer = n_sum % 9

    return answer