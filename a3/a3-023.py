def sieve(n):
    prime = [True]*(n+1)
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False
    return prime

def count_prime_triplets(A, B):
    max_sum = 3*B
    min_sum = 3*A

    prime = sieve(max_sum)
    prefix_prime = [0]*(max_sum+1)
    for i in range(min_sum, max_sum+1):
        prefix_prime[i] = prefix_prime[i-1] + (1 if prime[i] else 0)
    for i in range(min_sum-1, -1, -1):
        prefix_prime[i] = prefix_prime[min_sum-1]

    count = 0
    for x in range(A, B+1):
        for y in range(x, B+1):
            sum_min = x + y + y
            sum_max = x + y + B
            if sum_min > max_sum:
                continue
            if sum_max > max_sum:
                sum_max = max_sum
            count += prefix_prime[sum_max] - prefix_prime[sum_min -1]
    return count

if __name__ == "__main__":
    A, B = map(int, input().split())
    print(count_prime_triplets(A, B))
