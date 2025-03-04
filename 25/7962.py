def simple_deli(n):
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            return False
        i += 1
    return True

def f(n):
    i = 2
    arr = []
    while i <= n**0.5:
        if n % i == 0:
            if i % 1000 == 777 and simple_deli(i):
                arr.append(i)
            if (n//i) % 1000 == 777 and simple_deli(n//i):
                arr.append(n//i)
        i += 1
    if arr == []:
        return False
    return min(arr)


cnt = 0
num = 55_000_001
dct = {}

while cnt < 4:
    if f(num):
        dct[num] = f(num)
        cnt += 1
    num += 1
dict_num = sorted(dct.items(), key=lambda items: items[1])
for i in dict_num:
    print(i[0], i[1])