def f(number):
    summ = 0
    while number:
        if number % 31 <= 17:
            summ += number % 31
        number //= 31
    return summ

number = 3*(289**2024) + 81*(49**121) - 9*(16**81) - 6011
print(f(number))