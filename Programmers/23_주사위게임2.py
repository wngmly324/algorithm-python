def solution(a, b, c):
    answer = 0

    res1 = a + b + c
    res2 = a ** 2 + b ** 2 + c ** 2
    res3 = a ** 3 + b ** 3 + c ** 3

    if a == b and b == c and c == a:
        answer = res1 * res2 * res3
    elif a != b and b != c and c != a:
        answer = res1
    else:
        answer = res1 * res2

    return answer