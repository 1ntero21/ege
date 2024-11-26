from itertools import product

alh = 'ГЛУБИНА'
count = 0

for i in product(alh, repeat=7):
    word = ''.join(i)
    if len(set(word)) == 7:
        if word.index('Г') - word.index('А') > 1:
            print(word)
            count += 1
print(count)