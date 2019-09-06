# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

#sum of squares
summationOfSquares = 0
squareOfSummation = 0

for num in range(1, 101):
    squared = num**2
    summationOfSquares += squared
    num += 1
#print(summationOfSquares)

sumOfRange = 0
for numb in range(1, 101):
    sumOfRange += numb
squareOfSummation = sumOfRange**2
#print(squareOfSummation)

print(squareOfSummation - summationOfSquares)


