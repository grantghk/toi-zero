n = input().split()
start_color = n[0]
count = int(n[1])

colors = ["Red", "Green", "Blue"]
start_index = {"R": 0, "G": 1, "B": 2}[start_color]
rgb_list = [colors[(start_index + i) % 3] for i in range(count)]

print(" ".join(rgb_list))