N, K = map(int, input().split())
count = [0] * K
for _ in range(N):
    row = int(input())
    count[row-1] += 1

min_count = min(count)
leftover = N - K * min_count
print(leftover)