a = input()
b = input()

if len(a) < len(b):
    a += a[:len(b) - len(a)]
elif len(b) < len(a):
    b += b[:len(a) - len(b)]
    
symbols = ''
for ca, cb in zip(a, b):
    if ca.lower() in 'love' or cb.lower() in 'love':
        symbols += 'w'
    else:
        symbols += '$'

w_count = symbols.count('w')

if w_count % 2 == 1:
    max_streak = 0
    current = 0
    for ch in symbols:
        if ch == 'w':
            current += 1
            max_streak = max(max_streak, current)
        else:
            current = 0
    symbols += str(max_streak)
elif 'ww' not in symbols:
    symbols += '#'

print(symbols)
