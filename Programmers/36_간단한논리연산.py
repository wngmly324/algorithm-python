'''
def solution(x1, x2, x3, x4):
    answer = True

    if x1 == True or x2 == True:
        t1 = True
    else:
        t1 = False

    if x3 == False and x4 == False:
        t2 = False
    else:
        t2 = True

    if t1 == True and t2 == True:
        return answer
    else:
        answer = False
        return answer
'''
def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)