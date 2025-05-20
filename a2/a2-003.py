N = int(input())
H = list(map(int, input().split()))

count = 0
for i in range(N):
    left_ok = (i == 0) or (H[i] > H[i-1])
    right_ok = (i == N-1) or (H[i] > H[i+1])
    if left_ok and right_ok:
        count += 1

print(count)