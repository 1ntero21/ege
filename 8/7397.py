from itertools import product

alh = 'АБВЕОПРС'
count = 0

for i in product(alh, repeat=7):
    word = ''.join(i)
    if word[3] in 'ОЕ' and word[:3] != word[4:]:
        count += 1
        print(word)
print(count)