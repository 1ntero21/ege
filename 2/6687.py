from itertools import *

def f(x, y, z, w):
    return (x and y) or (y == z) or w

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(1, a1, a2, 0), (0, 1, a3, a4), (1, 0, a5, 1)]
    if len(set(table)) == 3:
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(p)