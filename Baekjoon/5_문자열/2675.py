n = int(input())

for i in range(n):
    s = input()
    num = int(s[0])
    string = s[2:]

    for j in range(len(string)):
        print(string[j] * num, end="")

    print()