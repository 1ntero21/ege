from itertools import *

def f1(x, y, z, w):
    return (w <= y) == (z <= x)

def f2(x, y, z, w):
    return (w <= y) and ((not x) == z)

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(0, a1, 0, 0), (0, 0, 0, a2), (0, 1, 1, a3)]
    if len(set(table)) == 3:
        for p in permutations('xyzw'):
            if [f1(**dict(zip(p, t))) for t in table] == [0, 0, a4]:
                if [f2(**dict(zip(p, q))) for q in table] == [1, a5, 0]:
                    print(p)