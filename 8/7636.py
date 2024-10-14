from itertools import product
alh = '0123456789AB'

count = 0
for i in product(alh, repeat=5):
    word = ''. join(i)
    max_sign = word.count('9') + word.count('A') + word.count('B')
    if word.count('7') == 1 and word[0] != '0' and max_sign < 4:
        print(word)
        count += 1
print(count)