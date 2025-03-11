from sys import *
setrecursionlimit(3200)

def f(n):
    if n < 7: return 7
    if n % 3 != 0: return 5 - f(n-1)
    return 3 + f(n-1)

print(print(f(3015)))