N = int(input())
cars = [tuple(map(int, input().split())) for _ in range(N)]

max_eff = -1
unsellable_count = 0

for i in range(N-1, -1, -1):
    price, eff = cars[i]
    if eff <= max_eff:
        unsellable_count += 1
    else:
        max_eff = eff

print(unsellable_count)