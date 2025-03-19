alh = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for x in alh[:22]:
    num_1 = int(f'A23{x}AC0', 22)
    num_2 = int(f'GB{x}21670', 22)
    summ = num_1 + num_2
    if summ % 21 == 0:
        print(summ // 22)