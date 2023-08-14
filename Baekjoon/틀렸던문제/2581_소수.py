n = int(input())
m = int(input())

num_sum = 0
result = []
for i in range(n, m+1):
    no = 0
    if i > 1:
        for j in range(2, i+1):
            if i % j == 0:
                no += 1

        if no == 1:
            num_sum += j
            result.append(i)

if num_sum == 0:
    print(-1)
else:
    print(num_sum)
    print(result[0])
