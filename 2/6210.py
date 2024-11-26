from itertools import *

def f(x, y, z, w):
    return not((((not w) <= (not y)) <= (not z)) <= x)


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(a1, a2, 1, 0), (a3, 1, a4, 1), (0, 1, a5, 0)]
    if len(set(table)) == 3:
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 0]:
                print(p)