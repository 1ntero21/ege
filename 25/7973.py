from fnmatch import *

dct = {}

for i in range(0, 10**9 + 1, 7521):
    if fnmatch(str(i), '?13*79*9'):
        dct[i] = sum(map(int, str(i)))

dict_num = sorted(dct.items(), key=lambda item: item[1])
for i in dict_num:
    print(i[0], i[1])