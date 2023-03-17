n = int(input())
clist = [500, 100, 50, 10, 5, 1]

change = 1000 - n
count = 0
for i in clist:
    count += change // i
    change = change % i

print(count)