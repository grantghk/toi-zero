age = int(input())
type = str(input()).lower()

if age < 18 or type == "s":
    print(20)
else:
    print(50)