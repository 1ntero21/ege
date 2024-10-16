number = 5**100

def f(number):
    count = 0
    while number:
        if number % 5 == 0:
            count += 1
        number //= 5
    return count

for x in range(1, 7051):
    num = number - x
    if f(num) == 3:
        print(x)