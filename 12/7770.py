for n in range(4, 10001):
    alh = '1' + '8'*n
    while '11' in alh or '444' in alh or '8888' in alh:
        if '11' in alh:
            alh = alh.replace('11', '4', 1)
        if '444' in alh:
            alh = alh.replace('444', '88', 1)
        if '8888' in alh:
            alh = alh.replace('8888', '1', 1)
    sum_digit = sum(map(int, alh))
    if sum_digit % 8 == 0:
        print(n)