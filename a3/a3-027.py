n, m = map(int, input().split())
grid = [input().split() for _ in range(n)]

row = 0
for i in grid:
    index = 0
    for j in i:
        if j == "*":
            try:
                if not grid[row + 1][index] == "*":
                    grid[row + 1][index] = "x"
            except:pass
        index += 1
    row += 1

row = 0
for i in grid:
    index = 0
    for j in i:
        if j == "*":
            try:
                if grid[row + 1][index] == "x":
                    grid[row + 1][index] = "*"
            except:pass
        index += 1
    row += 1
    
for row in grid:
    print(' '.join(str(cell) for cell in row))