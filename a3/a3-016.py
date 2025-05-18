import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
count = [0]*(M)
conds = []
T = [0]*M
rules_for_light = [[] for _ in range(N+1)]

for i in range(M):
    data = list(map(int, input().split()))
    k = data[0]
    cond = data[1:1+k]
    t = data[1+k]
    count[i] = k
    conds.append(cond)
    T[i] = t
    for c in cond:
        rules_for_light[c].append(i)

on = [False]*(N+1)
q = deque()
on[1] = True
q.append(1)

while q:
    light = q.popleft()
    for r in rules_for_light[light]:
        count[r] -= 1
        if count[r] == 0:
            if not on[T[r]]:
                on[T[r]] = True
                q.append(T[r])

print(sum(on))