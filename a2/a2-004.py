n = int(input())
plate = {}
count = 0

for i in range(n):
    j = int(input())
    if j in plate:
        plate[j] += 1
    else:
        plate[j] = 1
    count = max(count,plate[j])

print(count)