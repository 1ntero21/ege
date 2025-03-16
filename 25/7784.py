def f(n):
    i = 2
    arr = []
    while i <= n**0.5:
        if n % i == 0:
            arr.append(i)
            arr.append(n//i)
        if len(sorted(set(arr))) >= 3:
            return sum(sorted(set(arr))[-2:])
        i += 1
    if arr != []:
        return sum(sorted(set(arr))[-2:])
    return 0

dct = {}

for i in range(256_123_000, 256_234_001):
    if f(i) % 10000 == 1234:
        dct[i] = f(i)

dct = sorted(dct.items(), key=lambda item: item[1])[::-1]
for i in dct:
    print(i[0], i[1])