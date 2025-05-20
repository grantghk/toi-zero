L, N = map(int, input().split())
bridges = []
points = set()

for _ in range(N):
    A, B = map(int, input().split())
    bridges.append((A, B))
    points.add(A)
    points.add(B)

points = sorted(points)
test_points = set()

for i in range(len(points) - 1):
    mid = (points[i] + points[i + 1]) / 2
    test_points.add(mid)

max_count = 0
for point in test_points:
    count = 0
    for A, B in bridges:
        if A < point < B:
            count += 1
    max_count = max(max_count, count)

print(max_count)
