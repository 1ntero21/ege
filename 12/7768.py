alh = '*'*200
count = 0

while '****' in alh or '???' in alh:
    if '****' in alh:
        alh = alh.replace('****', '???', 1)
        count += 3
    alh = alh.replace('??', '*', 1)

print(count)