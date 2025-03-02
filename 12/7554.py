alh = '9'*81

while '33333' in alh or '999' in alh:
    if '33333' in alh:
        alh = alh.replace('33333', '99', 1)
    else:
        alh = alh.replace('999', '3', 1)

print(alh)