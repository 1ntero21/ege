number = 6**2030 + 6**100

def f(number):
    count = 0
    while number:
        if number % 6 == 0:
            count += 1
        number //= 6
    return count

max_zero = 0
for x in range(1, 2031):
    num = number - x
    if max_zero < f(num):
        max_zero = f(num)
print(max_zero)