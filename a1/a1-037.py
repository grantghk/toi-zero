roman_map = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'),  (90, 'XC'), (50, 'L'),  (40, 'XL'),
    (10, 'X'),   (9, 'IX'),  (5, 'V'),   (4, 'IV'),
    (1, 'I')
]
num = int(input())
roman = ""
for value, symbol in roman_map:
    while num >= value:
        roman += symbol
        num -= value
print(roman)