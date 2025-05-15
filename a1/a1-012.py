val = input().strip()
val2 = val[::-1]
oparetion = input().strip()
cal = eval(f"{int(val)}{oparetion}{int(val2)}")
if oparetion in ["*","+"] and len(str(val)) == 2:
    print(f"{val} {oparetion} {val2} = {cal}")