from itertools import product

alh = '012345678'
count = 0

for i in product(alh, repeat=6):
    word = ''.join(i)
    if word[-1] not in '23' and word[0] not in '01357' and word.count('1') > 1:
        print(word)
        count += 1
print(count)