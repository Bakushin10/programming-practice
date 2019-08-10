class Prime():

    def getNextPrime(self):
        i = 0
        while True:
            if self.isPrime(i):
                yield i
            i += 1

    def isPrime(self, num):
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    return False
            return True

p = Prime()
nextprime = p.getNextPrime() 
print(next(nextprime))
print(next(nextprime))
print(next(nextprime))
print(next(nextprime))
print(next(nextprime))
print(next(nextprime))
print(next(nextprime))
print(next(nextprime))
print(next(nextprime))
print(next(nextprime))
print(next(nextprime))
print(next(nextprime))
print(next(nextprime))
print(next(nextprime))
print(next(nextprime))