from itertools import *

def f(x, y, z, w):
    return (z == (not y)) and ((not x) or y) and w

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [(1, a1, a2, 0), (0, 0, a3, 1), (a4, a5, a6, 1)]
    if len(set(table)) == 3:
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
                print(p)