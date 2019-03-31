import sys

def primeDivisibility():
    line = sys.stdin.readline()
    print(line)
    primes = getPrimeNumber(int(line))

    k = primes[-1]
    k_1 = primes[-2] 
    k_2 = primes[-3]
    print(str("k") + " "+ str(k))
    print(str("k_1") + " "+ str(k_1))
    print(str("k_2") + " "+str(k_2))
    
    remin = (k%k_1)
    r = k_2 - remin
    print(remin)
    print(r)
    return r

def getPrimeNumber(n):
    """
        this function will return
        the list of prime number
    """
    primes = [0]
    for p in range(1, n + 1): 
        if p > 1:
            for n in range(2, p): 
                if (p % n) == 0: 
                    break
            else:
                primes.append(p)
    return primes
    
print(primeDivisibility())