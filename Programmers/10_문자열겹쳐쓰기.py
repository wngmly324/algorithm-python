def solution(my_string, overwrite_string, s):
    answer = ''
    ol = len(overwrite_string)

    answer += my_string[:s] + overwrite_string[:] + my_string[(s + ol):]

    return answer