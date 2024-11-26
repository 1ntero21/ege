from itertools import *

def f(x, y, z, w):
    return ((x <= (y and w)) and (z <= (x or y))) != w


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(a1, 1, a2, 0), (a3, 1, 1, 1), (1, a4, 1, 0)]
    if len(set(table)) == 3:
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
                print(p)