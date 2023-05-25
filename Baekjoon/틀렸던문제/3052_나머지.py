data = []

for _ in range(10):
    data.append(int(input()))

result = set()
for i in data:
    result.add(i % 42)

print(len(result))