def solution(my_string, n):
    answer = ''

    t = len(my_string) - n
    answer = my_string[t:]

    return answer