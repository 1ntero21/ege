for n in range(4, 10000):
    alh = '1' + '2'*n
    while '12' in alh or '322' in alh or '222' in alh:
        if '12' in alh:
            alh = alh.replace('12', '2', 1)
        if '322' in alh:
            alh = alh.replace('322', '21', 1)
        if '222' in alh:
            alh = alh.replace('222', '3', 1)
    if sum(map(int, alh)) == 15:
        print(n)
        break