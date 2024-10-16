from itertools import product

alh = sorted('КОМПАНИЯ')
count = 0
index = 1

for i in product(alh, repeat=6):
    word = ''.join(i)
    if word[0] != 'М' and word.count('И') == 3 and index % 2 == 1:
        count += 1
        print(word)
    index += 1
print(count)