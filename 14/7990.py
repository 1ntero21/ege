from itertools import product

alh = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for p in range(10, len(alh)):
    for x, y, z, w in product(alh[:p], repeat=4):
        if len(set([x, y, z, w])) != 4:
            continue
        num_1 = int(f'{y}09{x}', p)
        num_2 = int(f'{y}{y}7{w}', p)
        num_3 = int(f'{w}{z}{y}{z}{y}', p)
        if num_1 + num_2 == num_3:
            print(int(f'{x}{y}{z}{w}', p))