def f(number):
    count = 0
    while number:
        if number % 5 == 0:
            count += 1
        number //= 5
    return count


num = 4*625**1920 - 4*25**1940 - 3*5**1950 - 1960

for x in range(1, 1000):
    number = num + 4*125**x
    if f(number) == 1891:
        print(x)