N, C = map(int, input().split())
win_table = [list(map(int, input().split())) for _ in range(N)]

special_team = C - 1 if C != 0 else -1
special_used = False

teams = list(range(N))

while len(teams) > 1:
    next_round = []
    for i in range(0, len(teams), 2):
        t1, t2 = teams[i], teams[i+1]

        winner = win_table[t1][t2] - 1

        if not special_used:
            if t1 == special_team and winner != t1:
                winner = t1
                special_used = True
            elif t2 == special_team and winner != t2:
                winner = t2
                special_used = True

        next_round.append(winner)
    teams = next_round

print(teams[0] + 1)