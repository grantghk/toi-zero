s = input()
S = s.upper()

max_u = 0
i = 0
while i < len(S):
    if S[i] == 'B':
        count_u = 0
        j = i + 1
        while j < len(S) and S[j] == 'U':
            count_u += 1
            j += 1
        if count_u >= 2:
            if count_u > max_u:
                max_u = count_u
        i = j
    else:
        i += 1

if max_u > 0:
    print("Yes", max_u)
else:
    if 'B' in S:
        index_b = S.index('B')
        prefix = s[:index_b+1]
        suffix_len = len(s) - (index_b + 1)
        print(prefix + 'U' * suffix_len)
    else:
        repeat = (len(s) + 2) // 3
        result = ("BUU" * repeat)[:len(s)]
        print(result)