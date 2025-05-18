N, L = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(N)]
intervals.sort(key=lambda x: x[1])

count = 0
last_point = -1

for s, t in intervals:
    if last_point < s:
        count += 1
        last_point = t

print(count)
