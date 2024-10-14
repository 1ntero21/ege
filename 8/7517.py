from itertools import product

alh = sorted('ФОКУС')
count = 1

for i in product(alh, repeat=5):
    word = ''.join(i)
    if 'Ф' not in word and word.count('У') == 2:
        print(f"{count} -> {word}")
    count += 1