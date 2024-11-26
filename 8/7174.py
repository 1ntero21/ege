from itertools import product, repeat

alh = 'ГЛУБИНА'
count = 0

for i in product(alh, repeat=7):
    word = ''.join(i)
    if len(set(word)) == 7:
        if word.index('А') < word.index('Г') and word.index('И') < word.index('Г'):
            print(word)
            count += 1
print(count)