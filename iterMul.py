
# perform multiplication by successive addition

def iterMul(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


print iterMul(2,3)