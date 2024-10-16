from itertools import product

alh = sorted('ПРИВЫЧКА')
index = 1

for i in product(alh, repeat=5):
    word = ''.join(i)
    if index % 5 != 0 and all(q not in 'ИЫА' for q in word) and len(set(word)) == 5:
        print(f"{index} -> {word}")
        break
    index += 1
print(index - (index//5))