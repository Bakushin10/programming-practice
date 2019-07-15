def cycleDetection(n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    print(int(n ** 0.5))
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)
            

array = 20
print(cycleDetection(array))