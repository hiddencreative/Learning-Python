
def recurPower(base, exp):

    if exp == 0:
        base = 1.0000
        return base
    elif exp == 1:
        return base
    else:
        return base * recurPower(base, exp - 1)


print recurPower(-1.52, 2)
print recurPower(-1.25, 3)