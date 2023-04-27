while True:
    data = list(map(int, input().split()))

    if data[0] == 0 and data[1] == 0 and data[2] == 0:
        break

    m = max(data)
    data.remove(m)

    if sum(data) <= m:
        print("Invalid")
        continue

    data.append(m)
    if data[0] == data[1] and data[0] == data[2] and data[1] == data[2]:
        print("Equilateral")
    elif data[0] != data[1] and data[0] != data[2] and data[1] != data[2]:
        print("Scalene")
    else:
        print("Isosceles")