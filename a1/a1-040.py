cal_map ={
    1:100,
    2:120,
    3:200,
    4:60
}
total_cals = 0
while True:
    choice = int(input())
    if choice == 5:
        break
    total_cals += cal_map[choice]
print("Bye Bye")
print(f"Total Calories: {total_cals}")