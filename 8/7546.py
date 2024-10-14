from itertools import product

alh = '0123456789ABCD'
count = 0

for i in product(alh, repeat=5):
    word = ''.join(i)
    max_sign = word.count('B') + word.count('C') + word.count('D')
    if word[0] != '0' and word.count('9') == 1 and max_sign < 4:
        print(word)
        count += 1
print(count)