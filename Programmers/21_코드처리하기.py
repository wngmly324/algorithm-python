def solution(code):
    ret = ''

    mode = 0
    for idx, val in enumerate(code):
        if mode == 0:
            if val != '1' and idx % 2 == 0:
                ret += val
            elif val == '1':
                mode = 1
        else:
            if val != '1' and idx % 2 != 0:
                ret += val
            elif val == '1':
                mode = 0

    if len(ret) == 0:
        return "EMPTY"

    return ret