a = int(input())
b = int(input())
c = int(input())

s = a + b + c

if s != 180:
    print("Error")
elif a == b and a == c and b == c:
    print("Equilateral")
elif a != b and a != c and b != c:
    print("Scalene")
else:
    print("Isosceles")