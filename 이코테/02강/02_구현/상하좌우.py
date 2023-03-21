n = int(input())
move = list(input().split())

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print("(%d, %d)" % (i, j), end=" ")
#     print()

R, D = 1, 1
L, U = -1, -1

x = 1
y = 1
for i in range(len(move)):
    if move[i] == 'R':
        y = y + R
        if y < 1 or y > n:
            y = y - 1
    elif move[i] == 'D':
        x = x + D
        if x < 1 or x > n:
            x = x - 1
    elif move[i] == 'L':
        y = y + L
        if y < 1 or y > n:
            y = y + 1
    else:
        x = x + U
        if x < 1 or x > n:
            x = x + 1

print(x, y)

##############################################

# N 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)