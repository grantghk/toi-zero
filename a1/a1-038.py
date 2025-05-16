n = int(input())
text = ""
for _ in range(n):
    if (_+1)%5==0:
        text += "X"
    else:
        text += "*"
print(text)