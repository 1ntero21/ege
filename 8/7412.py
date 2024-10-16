from itertools import product

alh = sorted('ГЛУБИНА')[::-1]
count = 0
index = 1

for i in product(alh, repeat=6):
    word = ''.join(i)
    if word.count('Н') > 1 and word.count('А') > 1 and index % 2 == 1:
        if any((f"А{''.join(j)}А" in word) for j in product('ГЛУБИН', repeat=2)):
            count += 1
            print(f"{index} -> {word}")
    index += 1
print(count)