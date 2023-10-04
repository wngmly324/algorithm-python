def solution(arr, queries):
    answer = []

    for i in range(len(queries)):
        s = queries[i][0]
        e = queries[i][1]
        k = queries[i][2]

        res = []
        for j in range(s, e + 1):
            if arr[j] > k:
                res.append(arr[j])

        if len(res) > 0:
            answer.append(min(res))
        else:
            answer.append(-1)

    return answer
"""
def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        tmp = []
        
        for x in arr[s:e+1]:
            if x > k:
                tmp.append(x)
                
        answer.append(-1 if not tmp else min(tmp))
        
    return answer
"""