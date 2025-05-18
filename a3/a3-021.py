import math

size, target = map(int, input().split())
numbers = sorted(int(input()) for _ in range(size))

base = numbers[0]
min_required = base * target
valid_count = sum(1 for value in numbers if target == math.ceil(min_required / value))

print(valid_count)
