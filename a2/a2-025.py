def manhattan_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

n, m = map(int, input().split())
sx, sy = map(int, input().split())
k = int(input())

infected = [tuple(map(int, input().split())) for _ in range(k)]

risk_map = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        max_risk = 0
        for (x, y) in infected:
            dist = max(abs(i - x), abs(j - y))

            if dist == 0:
                risk = 100
            elif dist == 1:
                risk = 60
            elif dist == 2:
                risk = 20
            else:
                risk = 0
            
            if risk > max_risk:
                max_risk = risk
        risk_map[i][j] = max_risk

safe_count = sum(cell == 0 for row in risk_map for cell in row)
print(safe_count)
print(f"{risk_map[sx][sy]}%")
