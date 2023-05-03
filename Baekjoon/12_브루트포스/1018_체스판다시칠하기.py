n, m = map(int, input().split())
board = []
result = []

for i in range(n):
    board.append(input())

for a in range(n-7):
    for b in range(m-7):                    # 8*8로 자르기 위해, -7을 해준다.
        w_index = 0                         # 흰색으로 시작
        b_index = 0                         # 검은색으로 시작
        for i in range(a, a+8):             # 시작지점
            for j in range(b, b+8):         # 시작지점
                if (i+j) % 2 == 0:          # 짝수인 경우
                    if board[i][j] != 'W':  # W가 아니면, 즉 B이면
                        w_index += 1        # W로 칠하는 개수
                    else:
                        b_index += 1        # B로 칠하는 개수
                else:                       # 홀수인 경우
                    if board[i][j] != 'W':  # W가 아니면, 즉 B이면
                        b_index += 1        # B로 칠하는 개수
                    else:
                        w_index += 1        # W로 칠하는 개수
        result.append(w_index)              # W로 시작할 때 경우의 수
        result.append(b_index)              # B로 시작할 떼 경우의 수
print(min(result))