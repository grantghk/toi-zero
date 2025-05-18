N = int(input())
heights = [int(input()) for _ in range(N)]

heights.sort() 

total = 0
cumulative = 0
for h in heights:
    cumulative += h
    total += cumulative

print(total * 2)
