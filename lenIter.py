def lenIter(aStr):

    x = 0

    for char in aStr:
        x += 1
    return x


def lenRecur(aStr)

    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[1:])

