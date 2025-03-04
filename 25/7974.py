from fnmatch import *

dct = {}

for i in range(0, 10**9 + 1, 7863):
    if fnmatch(str(i), '?54*32*1'):
        dct[i] = sum(map(int, str(i)))

dict_num = sorted(dct.items(), key=lambda item: item[1])
for i in dict_num:
    print(i[0], i[1])