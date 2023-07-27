s = input().upper()
word = dict()

for i in s:
    if i in word:
        word[i] += 1
    else:
        word[i] = 1

max_value = max(word.values())

answer = []
for key, value in word.items():
    if value == max_value:
        answer.append(key)

if len(answer) > 1:
    print("?")
else:
    print(*answer)
