b_type,b_amount = input().split()
t_type,t_scale,t_amount = input().split()

tea = {
    "R": (12,18,25),
    "T": (15,20,30),
    "M": (10,15,20)
}
bubble = {
    "H":5,
    "O":3,
    "J":2
}

cals = bubble[b_type] * int(b_amount)
cals += tea[t_type][int(t_scale)-1] * int(t_amount)
print(cals)