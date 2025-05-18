number = int(input())

root = 0
while root * root < number:
    root += 1

adjust = 2 * (root - 1)
if (number % 2) != (root % 2):
    adjust -= 1

print(adjust)