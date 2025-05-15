temp = int(input())
type = str(input()).lower().strip()

def check_C(temp):
    if temp <= 0:
        return "solid"
    elif temp >= 100:
        return "gas"
    else:
        return "liquid"
    
def check_F(temp):
    if temp <= 32:
        return "solid"
    elif temp >= 212:
        return "gas"
    else:
        return "liquid"

if type == "f":
    print(check_F(temp)) 
elif type == "c":
    print(check_C(temp))