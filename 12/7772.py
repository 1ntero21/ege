for n in range(3, 10000):
    alh = '59' + '8'*n
    while '68' in alh or '988' in alh or '888' in alh:
        if '68' in alh:
            alh = alh.replace('68', '8', 1)
        if '988' in alh:
            alh = alh.replace('988', '86', 1)
        if '888' in alh:
            alh = alh.replace('888', '9', 1)
    summ_digit = sum(map(int, alh))
    if summ_digit**(1/3) == int(summ_digit**(1/3)):
        print(n)
        break