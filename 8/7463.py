from itertools import product

alh = '01234567'
count = 0

for i in product(alh, repeat=5):
    word = ''.join(i)
    if word[0] not in '01357' and word[-1] not in '26' and word.count('7') < 3:
        print(word)
        count += 1
print(count)