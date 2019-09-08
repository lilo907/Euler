# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10001st prime number?


def nthPrime(n):
    primeList = [2]
    num = 3
    while len(primeList) < n:
        for p in primeList:
            if num % p == 0:
                break
        else:
            primeList.append(num)
        num += 2
    print(primeList[-1])


nthPrime(10001)
