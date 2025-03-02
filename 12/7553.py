alh = '9'*136

while '22222' in alh or '9999' in alh:
    if '22222' in alh:
        alh = alh.replace('22222', '99', 1)
    else:
        alh = alh.replace('9999', '2', 1)

print(alh)