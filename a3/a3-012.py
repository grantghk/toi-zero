N, S = map(int, input().split())
forward = [0] * (N + 1)

for i in range(1, N + 1):
    forward[i] = int(input())

visited = [False] * (N + 1)

count = 0
current = S
while current != 0 and not visited[current]:
    visited[current] = True
    count += 1
    current = forward[current]

print(count)