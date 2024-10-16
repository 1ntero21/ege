from itertools import product

alh = '567'
count = 0

for i in product(alh, repeat=12):
    word = ''.join(i)
    if '55' not in word:
        count += 1
        print(word)
print(count)