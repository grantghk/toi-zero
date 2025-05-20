n, k = map(int, input().split())

in1 = sorted(map(int, input().split()))
in2 = sorted(map(int, input().split()))
out1 = sorted(map(int, input().split()))
out2 = sorted(map(int, input().split()))

mn = float('inf')

for i in range(min(n, k) + 1):
    j = k - i
    if j > n:
        continue

    mx = 0
    for x in range(i):
        mx = max(mx, in1[x] + out1[i - x - 1])

    for x in range(j):
        mx = max(mx, in2[x] + out2[j - x - 1])

    mn = min(mn, mx)

print(mn)
