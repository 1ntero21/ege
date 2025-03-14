from itertools import *

def f1(x, y, z, w):
    return (w <= z) == (y <= x)

def f2(x, y, z, w):
    return (w <= z) and ((not x) == y)

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(a1, 0, 0, 0), (a2, 0, 1, 1), (0, 0, a3, 0)]
    if len(set(table)) == 3:
        for p in permutations('xyzw'):
            if [f1(**dict(zip(p, t))) for t in table] == [0, a4, 0]:
                if [f2(**dict(zip(p, t))) for t in table] == [a5, 0, 1]:
                    print(p)