limit, remaining = map(int, input().split())

rounds = 0

while remaining > 0:
    rounds += 1
    step = 0
    while step < rounds * limit and remaining > 0:
        step += 1
        remaining -= min(step, limit)

print(rounds)