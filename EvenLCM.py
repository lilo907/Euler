# This program is for:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# the answer is given when the user inputs any set of numbers and it calculates the LCM
from functools import reduce

intList = [int(x) for x in input("Enter integers: ").split(" ")]
primeFacList = []


def countX(lst, x):
    count = 0
    for ele in lst:
        if ele == x:
            count = count + 1
    return count


def findPrimes(n):
    primeList = []
    p = 2
    while p * p <= n:
        while n % p == 0:
            primeList.append(p)
            n //= p
        p += 1
    if n > 1:
        primeList.append(n)
    return primeList


for num in intList:
    primeFacList.append(findPrimes(num))

print(set(sum(primeFacList, [])))
globalCountMap = {}
for subList in primeFacList:
    for prime in set(subList):
        if prime in globalCountMap:
            if subList.count(prime) > globalCountMap[prime]:
                globalCountMap[prime] = subList.count(prime)
        else:
            globalCountMap[prime] = subList.count(prime)

product = reduce(lambda x, y: x * y, [k**v for k, v in globalCountMap.items()])
print(product)

# total = 1
# for p in product:
#     total *= p
#
# print(total)



