def gomgomi(n):
    gomgom = set()
    cnt = 0

    for _ in range(n):
        s = input()

        if s != "ENTER":
            if s not in gomgom:
                cnt += 1
                gomgom.add(s)
        elif s == "ENTER":
            gomgom.clear()

    return cnt

print(gomgomi(int(input())))