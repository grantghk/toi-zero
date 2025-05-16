n = int(input())
numbers = list(map(int, input().split()))

greater_values = []

for i in range(0, 2 * n, 2):
    a = numbers[i]
    b = numbers[i + 1]
    greater_values.append(max(a, b))

if len(greater_values) == 1:
    print(greater_values[0])
else:
    equation = " + ".join(map(str, greater_values))
    total = sum(greater_values)
    print(f"{equation} = {total}")
