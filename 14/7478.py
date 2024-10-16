number = 5**100

def f(number):
    count = 0
    while number:
        if number % 5 == 0:
            count += 1
        number //= 5
    return count

for x in range(8300, 10000):
    num = number - x
    if f(num) == 4:
        print(x)