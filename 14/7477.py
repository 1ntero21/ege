number = 3**100

def f(number):
    count = 0
    while number:
        if number % 3 == 0:
            count += 1
        number //= 3
    return count

for x in range(4100, 10000):
    num = number - x
    if f(num) == 1:
        print(x)