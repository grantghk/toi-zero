N = int(input())
P = list(map(int, input().split()))

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + P[i - 1]

result_set = set()

for a in range(1, N + 1):
    for b in range(a, N + 1):
        total = prefix[b] - prefix[a - 1]
        result_set.add(total)

print(len(result_set))
