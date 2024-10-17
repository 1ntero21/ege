from itertools import *

def f(x, y, z, w):
    return (x or (not y)) and (not (x == z)) and (not w)

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(0, 0, 1, a1), (0, a2, 0, 1), (a3, 1, 1, a4)]
    if len(set(table)) == 3:
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
                print(p)