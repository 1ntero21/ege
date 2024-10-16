number = 7**91 + 7**160

def f(number):
    count = 0
    while number:
        if number % 7 == 0:
            count += 1
        number //= 7
    return count

for x in range(1, 2031):
    num = number - x
    if f(num) == 70:
        print(x)