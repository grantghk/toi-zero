from collections import defaultdict

N, W, L = map(int, input().split())
boards = []

for _ in range(N):
    _, *holes = map(int, input().split())
    boards.append(holes)

counter = defaultdict(int)

for holes in boards:
    seen = set()
    for hole in holes:
        for shift in range(-L, L + 1):
            new_pos = hole + shift
            if 1 <= new_pos <= W:
                seen.add(new_pos)
    for pos in seen:
        counter[pos] += 1

for v in counter.values():
    if v == N:
        print(1)
        break
else:
    print(0)
