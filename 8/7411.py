from itertools import product

alh = '012345678'
count = 0

for i in product(alh, repeat=7):
    word = ''.join(i)
    if word[0] not in '01357' and word.count('6') > 0 and word[-1] not in '036':
        count += 1
        print(word)
print(count)