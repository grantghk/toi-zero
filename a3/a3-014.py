N = int(input())
tasks = [int(input()) for _ in range(N)]

heavy = sum(1 for t in tasks if t > 18)
light = N - heavy

extra_rest = max(0, heavy - 1 - light)
days = N + extra_rest

print(days)
