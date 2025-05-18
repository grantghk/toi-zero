width, length, start, end = map(int, input().split())
candidates = [(width % divisor) * (length % divisor) for divisor in range(start, end + 1)]
print(min(candidates))