#sums up all multiples of 3 or 5 under a 1000

summation = 0

for i in range(3,1000):
    if i % 3 == 0:
        summation += i

    elif i % 5 == 0:
        summation += i

print(summation)