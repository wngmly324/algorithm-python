import sys

data = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

sum_hak = 0
sum_jum = 0
for _ in range(20):
    a, b, c = sys.stdin.readline().split()

    if c == "P":
        continue
    else:
        sum_hak += float(b)

        d = data.get(c)
        sum_jum += (float(b) * d)

print("%.6f" % (sum_jum / sum_hak))