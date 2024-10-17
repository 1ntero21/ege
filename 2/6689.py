from itertools import *

def f(x, y, z, w):
    return (x and (not y)) or (x == z) or w

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(1, a1, a2, a3), (1, 1, a4, a5), (a6, 1, a7, 1)]
    if len(set(table)) == 3:
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(p)