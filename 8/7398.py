from itertools import product

alh = 'АВР'
index = 1

for i in product(alh, repeat=7):
    word = ''.join(i)
    if word.count('А') == 3 and word.count('В') == 2 and word.count('Р') == 2:
        if index % 2 == 0 and word[0] == 'В' and 'ААА' in word and 'РР' not in word:
            print(f"{index} -> {word}")
        index += 1