import sys
sys.setrecursionlimit(10000)

N = int(input())
bars = [None]

for _ in range(N):
    A, L, B, R = map(int, input().split())
    bars.append((A, L, B, R))

added_weight = 0

def dfs(idx):
    global added_weight
    A, L, B, R = bars[idx]
    
    if A == 1:
        left_weight = L
    else:
        left_weight = dfs(L)
        
    if B == 1:
        right_weight = R
    else:
        right_weight = dfs(R)

    if left_weight > right_weight:
        added_weight += left_weight - right_weight
        right_weight = left_weight
    else:
        added_weight += right_weight - left_weight
        left_weight = right_weight

    return left_weight + right_weight

dfs(1)
print(int(added_weight))