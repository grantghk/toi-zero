n, m = map(int, input().split())
k = int(input())

grid = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    grid[x][y] += 1

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

max_catch = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] > 0:
            continue

        count = 0
        for d in range(8):
            ni = i + dx[d]
            nj = j + dy[d]
            if 0 <= ni < n and 0 <= nj < m:
                count += grid[ni][nj]
        max_catch = max(max_catch, count)

print(max_catch)