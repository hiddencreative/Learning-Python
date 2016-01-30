
def iterPower(base, exp):

    result = base

    if exp == 0:
        result = 1.0000
        return result

    else:
        while exp > 1:
            result *= base
            exp -= 1
        return result

print iterPower(3, 3)
print 3**3
