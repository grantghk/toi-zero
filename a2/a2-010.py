from bisect import bisect_left

n, q = map(int, input().split())

segments = []
current_depth = 0
position = 0

for _ in range(n):
    d, length = map(int, input().split())
    current_depth += d
    left = position
    position += length
    right = position
    segments.append((current_depth, left, right))

segments.append((0, position, float('inf')))

stack = [(0, 0, 0)]
depth_for_width = {}

for h, l, r in segments:
    while stack and stack[-1][0] >= h:
        prev_h, prev_l, prev_r = stack.pop()
        width = prev_r - prev_l
        depth_for_width[width] = max(depth_for_width.get(width, 0), prev_h)
        l = prev_l
    stack.append((h, l, r))

lookup = sorted((width, depth) for width, depth in depth_for_width.items())
lookup.append((float('inf'), 0))

for i in range(len(lookup) - 2, -1, -1):
    lookup[i] = (lookup[i][0], max(lookup[i][1], lookup[i + 1][1]))

for _ in range(q):
    w = int(input())
    idx = bisect_left(lookup, (w, float('-inf')))
    print(lookup[idx][1])
