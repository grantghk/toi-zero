char = str(input())
num = int(input())

password = "H".upper(),4567

if num == password[1] and char == password[0]:
    print("safe unlocked")
elif char == password[0]:
    print("safe locked - change digit")
elif num == password[1]:
    print("safe locked - change char" )
else:
    print("safe locked")