n, m = map(int, input().split())
bomb_count = int(input())
grid = [[0 for _ in range(m)] for _ in range(n)]
bombs = []

for _ in range(bomb_count):
    r, c = map(int, input().split())
    grid[r][c] = 'x'
    bombs.append((r, c))

directions = [(-1,-1), (-1,0), (-1,1),
              (0,-1),         (0,1),
              (1,-1),  (1,0), (1,1)]

for r, c in bombs:
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 'x':
            grid[nr][nc] += 1

for row in grid:
    print(' '.join(str(cell) for cell in row))