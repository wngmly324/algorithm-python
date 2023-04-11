data = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

s = []
g = []

sum1 = 0
sum2 = 0
for i in range(20):
    a, b, c = input().split()

    if c == "P":
        pass
    else:
        sum1 += float(b)
        sum2 += (float(b) * data[c])

print("%.6f" % (sum2 / sum1))