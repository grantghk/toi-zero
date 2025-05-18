matrix = [list(map(int, input().split())) for _ in range(5)]

odd_row = -1
for i in range(5):
    if sum(matrix[i]) % 2 != 0:
        odd_row = i
        break

odd_col = -1
for j in range(5):
    col_sum = sum(matrix[i][j] for i in range(5))
    if col_sum % 2 != 0:
        odd_col = j
        break

print(odd_row, odd_col)
