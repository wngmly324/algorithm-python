# n = int(input())
#
# res = 1
# for i in range(1, n+1):
#     res *= i
#
# print(res)

def my_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * my_factorial(n-1)

n = int(input())
print(my_factorial(n))