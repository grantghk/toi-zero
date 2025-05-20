nums=list(map(int,input().split()))
seen=set()
print(' '.join(str(x) for x in nums if not (x in seen or seen.add(x))))