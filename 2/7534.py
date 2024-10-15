print('x y z w')

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ((not x) and y and z and (not w)) or ((not x) and y and (not z) and (not w)) or (x and y and z and (not w)):
                    print(x, y, z, w)
# x  w  z  y