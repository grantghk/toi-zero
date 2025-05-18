N, L = map(int, input().split())
heights = list(map(int, input().split()))
customers = list(map(int, input().split()))

prefix_max = [0] * N
prefix_max[0] = heights[0]
for i in range(1, N):
    prefix_max[i] = max(prefix_max[i-1], heights[i])

for pos in customers:
    h = heights[pos-1]
    if pos == 1:
        print(0)
        continue

    max_front = prefix_max[pos-2] 
    if h > max_front:
        print(0)
    else:
        print(max_front - h + 1)