N = int(input())
u = []
v = []

for _ in range(N):
    x, y = map(int, input().split())
    u.append(x + y)
    v.append(x - y)

u.sort()
v.sort()
median_u = u[N // 2]
median_v = v[N // 2]

total = sum(abs(median_u - ui) for ui in u) + sum(abs(median_v - vi) for vi in v)

print(total)