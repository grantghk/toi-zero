size, type_ = input().upper().split()
topping_input = input().strip()

base_prices = {"S": (60, 80), "M": (80, 100), "L": (100, 120)}
topping_prices = {"P": 15, "E": 10}

total = base_prices[size][0] if type_ == "R" else base_prices[size][1]

if topping_input != "N":
    topping, amount = topping_input.split()
    total += topping_prices[topping] * int(amount)

print(total)