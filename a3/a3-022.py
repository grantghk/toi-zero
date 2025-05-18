N = int(input())
light = [False] * 360
for _ in range(N):
    A, B = map(int, input().split())
    if A < B:
        for i in range(A, B):
            light[i] = True
    else:
        for i in range(A, 360):
            light[i] = True
        for i in range(0, B):
            light[i] = True

max_len = 0
current = 0

for i in range(720):
    if light[i % 360]:
        current += 1
        max_len = max(max_len, current)
    else:        
        current = 0

print(max_len)