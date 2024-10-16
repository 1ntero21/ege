from itertools import product


alh = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for p in range(10, 37):
    for x, y, z, w in product(alh[:p], repeat=4):
        number_1 = int(f"{z}{x}{y}{x}9", p)
        number_2 = int(f"{x}{y}748", p)
        number_3 = int(f"{w}{z}{x}61", p)
        if number_1 + number_2 == number_3:
            print(int(f"{x}{y}{z}{w}", p))