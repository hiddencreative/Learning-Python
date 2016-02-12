
from math import factorial

def applyFuns(L,x):
    for f in L:
        print(f(x))

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)



applyFuns([abs, int, factorial, fib], 4)