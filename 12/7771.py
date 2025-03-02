from functools import reduce


for n in range(4, 10000):
    alh = '2' + '7'*n
    while '27' in alh or '777' in alh or '377' in alh:
        if '27' in alh:
            alh = alh.replace('27', '7', 1)
        if '777' in alh:
            alh = alh.replace('777', '3', 1)
        if '377' in alh:
            alh = alh.replace('377', '72', 1)
    prod = reduce(lambda x, y: x*y, map(int, alh))
    if prod % 3 == 0 and prod % 10 == 1:
        print(n)