n = int(input())
weights = []

for i in range(1, 201):
    weights.extend([i * 2] * 9)
    weights.append(i)

dr = list(map(int, input().split()))

dr.sort(reverse=True)
weights.sort()

count = sum(dr[i] * weights[i] for i in range(n))

print(count)