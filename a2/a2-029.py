n = int(input())

for i in range(n):
    for j in range(i + 1):
        if j == 0 or i == j or i == n - 1:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()