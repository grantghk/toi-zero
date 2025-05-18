N, M = map(int, input().split())

events = []

for _ in range(M):
    S, T = map(int, input().split())
    events.append((S, 'start'))
    events.append((T + 1, 'end'))

events.sort(key=lambda x: (x[0], 0 if x[1] == 'start' else 1))

max_active = 0
active = 0

for _, typ in events:
    if typ == 'start':
        active += 1
        max_active = max(max_active, active)
    else:
        active -= 1

print(max_active)
