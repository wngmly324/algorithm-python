import string

n, b = map(int, input().split())

tmp = string.digits + string.ascii_uppercase
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]

print(convert(n, b))