n = int(input())
vovel = ["a","e","i","o","u"]
print([1 if i in vovel else 0 for i in [str(input()).lower() for _ in range(n)]].count(1))