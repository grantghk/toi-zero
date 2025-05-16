n = int(input()) // 10
string = ""
for _ in range((n)*10,0,-10):
    string += f"{_} "
print(string+"0")