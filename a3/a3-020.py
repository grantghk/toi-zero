H1, H2, B1, B2 = map(int, input().split())
X, Y = map(int, input().split())

same_white = min(H1, B1)
same_black = min(H2, B2)
same_total = same_white + same_black
same_sell = min(X, same_total)

diff_white_head = min(H1, B2)
diff_black_head = min(H2, B1)
diff_total = diff_white_head + diff_black_head
diff_sell = min(Y, diff_total)

print(same_sell + diff_sell)
