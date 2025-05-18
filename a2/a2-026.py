n = int(input())

overweight_count = 0

max_weight = -1
fattest_rabbit_name = ""

for _ in range(n):
    name, weight = input().split()
    weight = int(weight)

    if weight > 15:
        overweight_count += 1

    if weight > max_weight:
        max_weight = weight
        fattest_rabbit_name = name

print(overweight_count)
print(fattest_rabbit_name, max_weight)