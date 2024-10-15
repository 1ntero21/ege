print('x y z w')

for x in 0, 1:
    for y in 0,1:
        for z in 0, 1:
            for w in 0, 1:
                if not(((w <= y) <= x) or (not z)):
                    print(x, y, z, w)

# z y  w x