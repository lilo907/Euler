# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def isLessThan(a, b, c):
    if a < b < c:
        return True


def pyTheorem(a, b, c):
    if isLessThan(a, b, c):
        if a ** 2 + b ** 2 == c ** 2:
            return True


for z in range(0, 1000):
    for y in range(0, z):
        for x in range(0, y):
            if isLessThan(x, y, z) and x + y + z == 1000:
                if pyTheorem(x, y, z):
                    print(x)
                    print(y)
                    print(z)



