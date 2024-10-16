number = 7**100

def f(number):
    count = 0
    while number:
        if number % 7 == 0:
            count += 1
        number //= 7
    return count

for x in range(5000, 100000):
    num = number - x
    if f(num) == 5:
        print(x)