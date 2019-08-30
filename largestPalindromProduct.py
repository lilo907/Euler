# computes the largest palidrome as a product of two 3 digit numbers
palinList = []


def reverse(prodToStr):
    return strProd[::-1]


def isPalin(prodToStr):
    rev = reverse(prodToStr)
    if rev == prodToStr:
        return True
    return False


for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        prod = num1 * num2
        strProd = str(prod)
        reverse(strProd)
        checkIf = isPalin(strProd)

        if checkIf == 1:
            palinList.append(int(strProd))
        else:
            pass
palinList.sort()
print(palinList[-1])
