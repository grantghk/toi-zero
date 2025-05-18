L, N = map(int, input().split())
layers = [i*i for i in range(1, L+1)]

for i in range(L):
    if N >= layers[i]:
        N -= layers[i]
        layers[i] = 0
    else:
        layers[i] -= N
        N = 0
        break

remaining_layers = sum(1 for x in layers if x > 0)

print(remaining_layers)
