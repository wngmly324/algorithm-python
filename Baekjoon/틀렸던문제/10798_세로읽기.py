data = [list(input()) for _ in range(5)]
result = []

for i in range(5):
    tmp = ['*' for _ in range(15)]

    for j in range(len(data[i])):
        tmp[j] = data[i][j]

    result.append(tmp)

for i in range(15):
    for j in range(5):
        s = result[j][i]

        if s == '*':
            pass
        else:
            print(s, end='')