length = int(input())
seq1 = list(map(int, input().split()))
seq2 = list(map(int, input().split()))

prev1, prev2 = 1, 1
overlap_count = 0

for i in range(length):
    low1, high1 = min(prev1, seq1[i]), max(prev1, seq1[i])
    low2, high2 = min(prev2, seq2[i]), max(prev2, seq2[i])

    if low1 == low2 and high1 == high2:
        overlap_count += 1
    elif low1 != low2 and high1 != low2 and low1 != high2 and high1 != high2:
        if (low1 < low2 < high1) or (low2 < low1 < high2):
            overlap_count += 1

    prev1, prev2 = seq1[i], seq2[i]

print(overlap_count)