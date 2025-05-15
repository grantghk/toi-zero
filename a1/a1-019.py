val1,val2,val3 = int(input()),int(input()),int(input())
list = [val1,val2,val3]
flagged = 0

before = None
for _ in list:
    if not before:
        before = _
    
    if before == _:
        flagged += 1

if flagged == 3:
    print("all the same")
elif flagged == 2:
    print("neither")
else:
    print("all different")