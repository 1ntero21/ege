from itertools import product


alh = sorted('АЭРОБУС')
count = 0
index = 1

for i in product(alh, repeat=5):
    word = ''.join(i)
    if word.count('Р') > 1 and word.count('У') == 0 and index % 2 ==0:
        if any((f"Р{j}Р" in word) for j in 'АЭОБУС'):
            print(f"{index} -> {word}")
            count += 1
    index += 1
print(count)