from itertools import product

alh = '012345678'
count = 0

for i in product(alh, repeat=5):
    word = ''.join(i)
    if word[0] != '0' and word.count('0') == 1:
        index = word.find('0')
        if word[index-1] not in '1357' and (word[index+1:index+2] not in '1357' or word[index+1:index+2] == ''):
            print(word)
            count += 1
print(count)
