N = int(input())

code1,code2 = input(),input()

wrong_positions = 0
for i in range(N):
    if int(code1[i]) + int(code2[i]) != 9:
        wrong_positions += 1

if wrong_positions == 0:
    print("YES")
else:
    print("NO", wrong_positions)
