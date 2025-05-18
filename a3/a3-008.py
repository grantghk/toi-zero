import sys
input = sys.stdin.readline

N, K = map(int, input().split())
colors = [int(input()) for _ in range(N)]

count = {}
distinct = 0
left = 0
result = 0

for right in range(N):
    c = colors[right]
    count[c] = count.get(c, 0) + 1
    if count[c] == 1:
        distinct += 1

    while distinct >= K:
        result += N - right
        left_color = colors[left]
        count[left_color] -= 1
        if count[left_color] == 0:
            distinct -= 1
        left += 1

print(result)