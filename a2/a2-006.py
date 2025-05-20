n = int(input())
grid = [list(input()) for _ in range(n)]
move = [[False]*n for _ in range(n)]

if grid[n-1][n-1] == '.':
    move[n-1][n-1] = True

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if grid[i][j] == '.':
                if i+1 < n and move[i+1][j]:
                    move[i][j] = True
                if j+1 < n and move[i][j+1]:
                    move[i][j] = True

count = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == '.' and move[i][j]:
            count += 1

print(count)
