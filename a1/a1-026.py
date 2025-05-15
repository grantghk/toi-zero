data = ["even" if _ % 2 == 0 else "odd" for _ in [int(input()) for _ in range(3)]]
even = data.count("even")
odd = data.count("odd")
print(f"even {even}")
print(f"odd {odd}")