def solution(my_string, is_suffix):
    tmp = len(my_string) - len(is_suffix)

    if my_string[tmp:] == is_suffix:
        answer = 1
    else:
        answer = 0

    return answer