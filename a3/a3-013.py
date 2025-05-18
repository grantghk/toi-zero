N, S = map(int, input().split())
heights = [int(input()) for _ in range(N)]

min_cross = 0
max_cross = 0

for h in heights:
    divisible_by_3 = (h % 3 == 0)
    divisible_by_4 = (h % 4 == 0)
    
    if divisible_by_3 and not divisible_by_4:
        H = h // 3
        dist = 10 * H
        min_cross += dist
        max_cross += dist
    elif divisible_by_4 and not divisible_by_3:
        H = h // 4
        dist = 10 * H
        min_cross += dist
        max_cross += dist
    else:
        H1 = h // 3
        H2 = h // 4
        dist1 = 10 * H1
        dist2 = 10 * H2
        min_cross += min(dist1, dist2)
        max_cross += max(dist1, dist2)

min_flat = S - max_cross
max_flat = S - min_cross

print(min_flat, max_flat)
