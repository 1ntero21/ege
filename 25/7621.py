def f(n):
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            return i + n// i
        i += 1
    return 0

cnt = 0
num = 800_001

while cnt < 5:
    if f(num) % 10 == 4:
        print(num, f(num))
        cnt += 1
    num += 1