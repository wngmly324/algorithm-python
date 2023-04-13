data = []
length = []

for _ in range(5):
    x = input()
    data.append(x)
    length.append(len(x))

string = ""
for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            string += data[j][i]

print(string)