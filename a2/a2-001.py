n, m = map(int, input().split())
red = [0] + list(map(int, input().split()))
blue = [0] + list(map(int, input().split()))

def segments_intersect(r1, r2, b1, b2, same_parity):
    if same_parity:
        return (r1 < b1 and r2 > b2) or (r1 > b1 and r2 < b2)
    else:
        return (r1 < b2 and r2 > b1) or (r2 > b1 and r1 < b2)

count = 0
for i in range(n):
    for j in range(m):
        same_parity = (i % 2) == (j % 2)
        if segments_intersect(red[i], red[i+1], blue[j], blue[j+1], same_parity):
            count += 1

for i in range(n+1):
    start = i % 2
    for j in range(start, m+1, 2):
        if red[i] == blue[j]:
            count += 1

print(count)