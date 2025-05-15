citizen_id = input().strip()

if citizen_id.isdigit() and len(citizen_id) == 13:
    print("yes")
else:
    print("no")
