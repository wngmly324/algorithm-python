x = int(input())

line = 1
while x > line:
    x -= line           # n -= line을 하면 각 line에서 n이 몇 번째에 위치하는지 알 수 있다
    line += 1

if line % 2 == 0:       # 짝수일 때는 분모 -1씩, 분자 +1씩
    a = x
    b = line - x + 1
else:                   # 홀수일 때는 분모 +1씩, 분자 -1씩
    a = line - x + 1
    b = x

print("%d/%d" % (a, b))
