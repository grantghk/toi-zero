n, m = map(int, input().split())
grid1 = [input() for _ in range(n)]
grid2 = [input() for _ in range(n)]
grid_out = [["-" for _ in range(m)] for _ in range(n)]

def find_intersec(v1, v2):
    if v1 == "-" and v2 == "-":
        return "-"
    elif v1 == "-" and v2 == "+":
        return "+"
    elif v1 == "-" and v2 == "x":
        return "x"
    elif v1 == "+" and v2 == "x":
        return "*"
    else:
        return "+"

for i in range(n):
    for j in range(m):
        grid_out[i][j] = find_intersec(grid1[i][j], grid2[i][j])

for row in grid_out:
    print(''.join(row))