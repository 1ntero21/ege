print('x y z w')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if not(not(x <= z) or (y == w) or y):
                    print(x, y, z, w)
#  z x y w