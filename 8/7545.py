from itertools import product

alh = '0123456789ABCDE'
count = 0

for i in product(alh, repeat=5):
    word = ''.join(i)
    max_sign = word.count('A') + word.count('B') + word.count('C') + word.count('D') + word.count('E')
    if word[0] != '0' and word.count('8') == 1 and max_sign > 1:
        print(word)
        count += 1
print(count)