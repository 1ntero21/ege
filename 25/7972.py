from fnmatch import *

dct = {}

for i in range(0, 10**9 + 1, 8587):
    if fnmatch(str(i), '?05*22*3'):
        dct[i] = sum(map(int, str(i)))

dict_num = sorted(dct.items(), key=lambda item: item[1])
for i in dict_num:
    print(i[0], i[1])