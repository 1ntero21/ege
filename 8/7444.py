from itertools import product

alh = '01234567'
count = 0

for i in product(alh, repeat=6):
    word = ''.join(i)
    if word.count('4') == 2 and '44' not in word and word[0] != '0' and len(set(word)) == 5:
        index = [j for j, x in enumerate(word) if x == '4']
        number = word[index[0]+1 : index[1]]
        if all([int(q) > 4 for q in number]):
            print(word)
            count += 1
print(count)