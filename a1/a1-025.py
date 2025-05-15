data = input().strip()
value = data[:-1].upper()
kind = data[-1:].upper()

kind_list = {
    "S" : "spades",
    "H" : "hearts",
    "D" : "diamonds",
    "C" : "clubs"
}
value_list = {
    "A" : "ace",
    "J" : "jack",
    "Q" : "queen",
    "K" : "king",
    "1" : "ace"
}
print(f"{value_list[value]} of {kind_list[kind]}" if value in value_list else f"{value} of {kind_list[kind]}")