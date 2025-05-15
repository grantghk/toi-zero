year = int(input())
cc = int(input())

if year <= 1990:
    if cc <= 1500:
        print("1250")
    elif cc > 1500 and cc <= 2000:
        print("1400")
    elif cc > 2000:
        print("2000")
elif year >= 1991 and year <= 1999:
    if cc <= 1500:
        print("1100")
    elif cc > 1500 and cc <= 2000:
        print("1300")
    elif cc > 2000:
        print("1700")
elif year <= 2000:
    if cc <= 1500:
        print("1000")
    elif cc > 1500 and cc <= 2000:
        print("1200")
    elif cc > 2000:
        print("1500")