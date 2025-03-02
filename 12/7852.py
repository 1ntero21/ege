count = 0

for n in range(12345, 14568):
    alh = '1'*n
    while '111' in alh:
            alh = alh.replace('111', '2', 1)
            alh = alh.replace('222', '11', 1)
            alh = alh.replace('1', '2', 1)
    if len(alh) == 3:
        count += 1

print(count)