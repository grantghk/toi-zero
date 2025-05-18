L, P = map(int, input().split())
r, m, f = map(int, input().split())

points = {}
for _ in range(P):
    pos, score = map(int, input().split())
    points[pos] = score

def calc_score(step):
    pos = 0
    total = 0
    while pos <= L:
        if pos in points:
            total += points[pos]
        pos += step
    return total

scores = {
    "Rabbit": calc_score(r),
    "Monkey": calc_score(m),
    "Frog": calc_score(f)
}

max_score = max(scores.values())

for animal in ["Rabbit", "Monkey", "Frog"]:
    if scores[animal] == max_score:
        print(animal, max_score)