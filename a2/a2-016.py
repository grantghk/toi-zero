base_char,base_num = input().split()
u_char,u_num = input().split()

rules = {
    1_000_000 : bool(base_char == u_char and base_num == u_num),
    100_000 : bool(base_num == u_num),
    2000 : bool(base_char == u_char and base_num[::-1][0:3] == u_num[::-1][0:3]),
    1000 : bool(base_char == u_char and base_num[::-1][0:2] == u_num[::-1][0:2]),
    200 : bool(base_num[::-1][0:3] == u_num[::-1][0:3]),
    100 : bool(base_num[::-1][0:2] == u_num[::-1][0:2]),
    20 : bool(base_char == u_char)
}

for i,j in rules.items():
    if j:
        print(i)
        exit()
print(0)