c = int(input())

for _ in range(c):
    data = []
    grade = []

    data = list(map(int, input().split()))

    grade = data[1:]
    s = sum(grade)
    avg = s / data[0]

    num = 0
    for j in grade:
        if j > avg:
            num += 1

    print("%.3f" % (num / data[0] * 100) + "%")