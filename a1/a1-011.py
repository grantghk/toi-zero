string = str(input())
cache = {}
for _ in [_ for _ in string]:
    if not cache.get(_):
        cache[_] = 1
    else:
        cache[_] += 1
        
print("".join([f"{_[1]}{_[0]}" for _ in cache.items()]))