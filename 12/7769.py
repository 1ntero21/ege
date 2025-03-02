max_sum = 0

for n in range(4, 10000):
    alh = 'C' + '4'*n
    while '444' in alh or '4A' in alh or 'AAAAA' in alh:
        if '444' in alh:
            alh = alh.replace('444', 'A4', 1)
        if '4A' in alh:
            alh = alh.replace('4A', 'A4', 1)
        if 'AAAAA' in alh:
            alh = alh.replace('AAAAA', '4', 1)
    max_sum = max(max_sum, sum(map(lambda x: int(x, 16), alh)))

print(max_sum)