from sys import *
setrecursionlimit(2500)

def f(n, x):
    if n >= 3000: return n
    return n + 2*x + f(n+2, x)

for x in range(0, 100):
    if f(28, x) - f(34, x) == 324:
        print(x)