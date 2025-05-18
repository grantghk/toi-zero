n = int(input())
scores = [int(input()) for _ in range(n)]

print(max(scores))
print(scores.count(max(scores)))