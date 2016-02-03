def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    exp=0
    i=start
    while i < stop:
        exp = exp + (f(i)*step)
        i += step
    return float(exp)
