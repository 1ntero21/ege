from itertools import product

alh = '01234567'
count = 0

for i in product(alh, repeat=6):
    word = ''.join(i)
    if word[0] != '0' and '33' not in word and word.count('3') == 2:
        index = [int(j) for j, x in enumerate(word) if x == '3']
        if all(int(q) > 3 for q in word[index[0] + 1: index[1]]):
            print(word)
            count += 1
print(count)