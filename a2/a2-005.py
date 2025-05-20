W, H, M, N = map(int, input().split())
Xs = list(map(int, input().split()))
Ys = list(map(int, input().split()))

Xs = [0] + Xs + [W]
Ys = [0] + Ys + [H]

widths = [Xs[i+1] - Xs[i] for i in range(len(Xs) - 1)]
heights = [Ys[i+1] - Ys[i] for i in range(len(Ys) - 1)]

areas = [w * h for w in widths for h in heights]

areas.sort(reverse=True)
print(areas[0], areas[1])
