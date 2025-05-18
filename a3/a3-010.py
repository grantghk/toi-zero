N, K, T = map(int, input().split())
current = 1
count = 1
while True:
    next_person = (current + K - 1) % N + 1
    if next_person == T:
        count += 1
        break
    if next_person == 1:
        break
    count += 1
    current = next_person
print(count)