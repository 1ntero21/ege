print('x y z w')

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not ((w or x or y) <= ((y or z) and x or y and (w or z))):
                    print(x, y, z, w)

# x y z w
# 1 0 0 0

# 0 0 1 1
# 1 0 0 1

# y w z x