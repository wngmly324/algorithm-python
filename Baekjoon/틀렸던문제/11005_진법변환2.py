n, b = map(int, input().split())

nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ''

while n:
    ans = nums[n % b] + ans
    n //= b

print(ans)