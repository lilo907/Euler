#this program finds the sum of all the even numbers of the Fibonacci sequence that are below 4,000,000

summation = 0
#termList = [] -------------used to check if sequence was displayed
term1 = 0
term2 = 1

for term in range(0, 4000000):
    nextTerm = term1 + term2
    term1 = term2 #update the term1
    term2 = nextTerm #update the term2
    #termList.append(nextTerm)----------used for testing purposes
    if nextTerm >= 4000000: #check if the next term is below 4,000,000
        break
    if nextTerm % 2 == 0: #check if it is even, if so, add it to the summation
        summation += nextTerm

#print(termList) ------------used to test
print(summation)
