coin = int(input())
store = {
    10 : 0,
    5 : 0,
    2 : 0,
    1 : 0
}
for i in store:
    store[i] = coin//i
    coin -= store[i] * i
    print(f"{i} = {store[i]}")