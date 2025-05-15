month = int(input())
day = int(input())

season = {
    "winter" : [1,2,3],
    "spring" : [4,5,6],
    "summer" : [7,8,9],
    "fall" : [10,11,12]
}

if day >= 21:
    if month == 12:
        month = 1
    month += 1
for i in season:
    if month in season[i]:
        print(i)