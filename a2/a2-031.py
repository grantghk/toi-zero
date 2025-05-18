def is_matching_pair(a, b):
    return (a == 'A' and b == 'T') or \
           (a == 'T' and b == 'A') or \
           (a == 'C' and b == 'G') or \
           (a == 'G' and b == 'C')

length = int(input())
chrom1 = input().split()
chrom2 = input().split()
n = int(input())

for _ in range(n):
    line, pos, new_gene = input().split()
    pos = int(pos)
    if line == '1':
        chrom1[pos] = new_gene
    else:
        chrom2[pos] = new_gene

print(' '.join(chrom1))
print(' '.join(chrom2))

wrong_pairs = 0
for a, b in zip(chrom1, chrom2):
    if not is_matching_pair(a, b):
        wrong_pairs += 1

print(wrong_pairs)
