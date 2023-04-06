s = input()

if '5' not in s and '6' not in s:
    a, b = s.split(" ")
    min = int(a) + int(b)
    max = int(a) + int(b)
else:
    smin = s.replace('6', '5')
    a, b = smin.split(" ")
    min = int(a) + int(b)

    smax = s.replace('5', '6')
    a, b = smax.split(" ")
    max = int(a) + int(b)

print(min, max)