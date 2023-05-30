x = int(input())

# n -= line을 하면 각 line에서 n이 몇 번째에 위치하는지 알 수 있다
line = 1
while x > line:
    x -= line
    line += 1

# line이 짝수일 때와 홀수이 때 분모, 분자의 증감 양상이 다르다
if line % 2 == 0:           # 짝수일 때는 분모 -1씩, 분자 +1씩
    up = x
    down = line - x + 1
else:                       # 홀수일 때는 분모 +1씩, 분자 -1씩
    up = line - x + 1
    down = x

print("%d/%d" % (up, down))