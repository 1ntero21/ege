number = 6**260 + 6**160 + 6**60

def f(number):
    count = 0
    while number:
        if number % 6 == 0:
            count += 1
        number //= 6
    return count

for x in range(1, 2031):
    num = number - x
    if f(num) == 202:
        print(x)