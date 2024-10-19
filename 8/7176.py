from itertools import product

alh = 'АБВГДЕ'
count = 1

for i in product(alh, repeat=4):
    word = ''.join(i)
    if (word[0] == 'А' and word[1] in 'АЕ') or (word[0] in 'БВГ' and word[1] in 'БВГД'):
        if word[2] in 'БВДЕ' and word[2] not in word[:2]:
            if word[-1] in 'БВГД' and word[-1] not in word[1:3]:
                print(f"{count} -> {word}")
                if word == 'ГВЕД':
                    break
                count += 1