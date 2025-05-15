inte = int(input())
if inte <= 0:
    print("Error : Please input positive number")
elif not inte in [_ for _ in range(10)]:
    print("Error : Out of range")
else:
    roman = ["I","II","III","IV","V","VI","VII","VIII","IX"]
    print(roman[inte-1])