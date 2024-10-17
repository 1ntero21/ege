from itertools import *

def f1(x, y, z, w):
    return (x <= y) or (not(w) == z)

def f2(x, y, z, w):
    return (x <= y) == (w and (not z))

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [(a1, a2, a3, 0), (a4, a5, 0, 0), (a6, 0, 0, 0)]
    if len(set(table)) == 3:
        for p in permutations('xyzw'):
            if [f1(**dict(zip(p, t))) for t in table] == [f2(**dict(zip(p, q))) for q in table]:
                print(p)