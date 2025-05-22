n = int(input())
mp1 = {}
mp2 = {}

for _ in range(n):
    x, y = map(int, input().split())

    key1 = x - y
    key2 = x + y

    if key1 not in mp1:
        mp1[key1] = [x, x]
    else:
        mp1[key1][0] = min(mp1[key1][0], x)
        mp1[key1][1] = max(mp1[key1][1], x)

    if key2 not in mp2:
        mp2[key2] = [x, x]
    else:
        mp2[key2][0] = min(mp2[key2][0], x)
        mp2[key2][1] = max(mp2[key2][1], x)

max_side = 0

for x_min, x_max in mp1.values():
    max_side = max(max_side, x_max - x_min)

for x_min, x_max in mp2.values():
    max_side = max(max_side, x_max - x_min)

print(max_side)
