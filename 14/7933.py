alh = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for x in alh[:25]:
    num_1 = int(f'11353{x}12', 25)
    num_2 = int(f'135{x}21', 25)
    summ = num_1 + num_2
    if summ % 24 == 0:
        print(summ // 24)