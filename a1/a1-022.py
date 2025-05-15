day = int(input())
month = int(input())

zodiac_conditions = {
    "capricorn": (month == 12 and day >= 22) or (month == 1 and day <= 19),
    "aquarius": (month == 1 and day >= 20) or (month == 2 and day <= 18),
    "pisces": (month == 2 and day >= 19) or (month == 3 and day <= 20),
    "aries": (month == 3 and day >= 21) or (month == 4 and day <= 19),
    "taurus": (month == 4 and day >= 20) or (month == 5 and day <= 20),
    "gemini": (month == 5 and day >= 21) or (month == 6 and day <= 21),
    "cancer": (month == 6 and day >= 22) or (month == 7 and day <= 22),
    "leo": (month == 7 and day >= 23) or (month == 8 and day <= 22),
    "virgo": (month == 8 and day >= 23) or (month == 9 and day <= 22),
    "libra": (month == 9 and day >= 23) or (month == 10 and day <= 23),
    "scorpio": (month == 10 and day >= 24) or (month == 11 and day <= 21),
    "sagittarius": (month == 11 and day >= 22) or (month == 12 and day <= 21)
}

for i,v in zodiac_conditions.items():
    if v:
        print(i)