def solution(arr, queries):
    answer = []

    for i in range(len(queries)):
        a = queries[i][0]
        b = queries[i][1]
        c = arr[a]

        arr[a] = arr[b]
        arr[b] = c

        answer = arr

    return answer
"""
def solution(arr, queries):
    for a, b in queries:
        arr[a], arr[b] = arr[b], arr[a]
    return arr
"""